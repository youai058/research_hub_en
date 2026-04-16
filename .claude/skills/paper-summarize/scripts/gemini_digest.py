#!/usr/bin/env python3
"""
gemini_digest.py — Stage 1 of the 2-stage paper summarization pipeline.

Reads a paper-hunter raw.md, downloads the full PDF via a 4-way fallback,
parses it with pymupdf, and asks the Gemini CLI (gemini-3-pro-preview) to produce a
dense, faithful content digest. Given a raw.md at papers/metadata/<V>/<Y>/<slug>.raw.md,
the digest is written to papers/digest/<V>/<Y>/<slug>.digest.md, the PDF cache to
papers/digest/<V>/<Y>/.pdf_cache/<slug>.pdf, and key figures to
papers/marp-summary/<V>/<Y>/.figure_cache/<slug>.png.

Usage:
    python3 gemini_digest.py <raw_md_path> [--force]

Exit codes:
    0  digest written (or skipped because cache is valid)
    2  raw.md not found / unreadable / frontmatter missing
    3  PDF could not be obtained
    4  pymupdf parse failed or full_text too short
    5  gemini CLI missing, timed out, errored, or returned empty output
    6  unexpected error

Stdout: absolute path of the digest file on success (exactly one line).
Stderr: human-readable logs.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import os
import re
import subprocess
import sys
import traceback
from pathlib import Path
from typing import Optional, Tuple

import urllib.request
import urllib.error

# -------- constants --------------------------------------------------------

PROMPT_VERSION = "v6"
GEMINI_MODEL = "gemini-3-pro-preview"
GEMINI_TIMEOUT_SEC = 600
MIN_FULLTEXT_CHARS = 3000
KST = _dt.timezone(_dt.timedelta(hours=9))
FIGURE_DPI_MATRIX = 3  # ~216 DPI at fitz default 72 DPI
FIGURE_MIN_BYTES = 10 * 1024  # 10KB sanity threshold
FIGURE_MIN_HEIGHT_FRAC = 0.10  # refined bbox must be >=10% of page height

DIGEST_PROMPT = """You are extracting a DENSE, FAITHFUL content digest of a research paper. The paper's full text has been provided above via stdin.

**CRITICAL CONTEXT**: The downstream agent (Claude) will NOT have access to the PDF. It writes the final summary using ONLY your digest + the paper's abstract metadata. Therefore your digest must contain every equation, every number, every hyperparameter, every result, and enough narrative context to let Claude later decide an adaptive section layout. Under-extraction here = broken summary downstream.

Your job is to extract as much content as possible from the paper, following the paper's own structure. Do NOT reorganize into a fixed template — mirror the paper's section layout.

## Instructions

1. **Start with metadata**: Title, authors, venue, year (verbatim).

2. **Author's framing (new)**: Immediately after metadata, add a short `## Author Framing` block:
   - One-sentence restatement of what the paper claims to show (as the authors themselves phrase it).
   - One sentence on the core intuition / mechanism in plain language.
   - 2–4 bullets listing the stated contributions, in the authors' own wording.
   This block exists so the downstream agent can write a faithful TL;DR without re-reading the PDF.

3. **Follow the paper's own sections**: Use the same section headings the paper uses (e.g., "Introduction", "Related Work", "Preliminary", "Method", "Experiments", etc.). If the paper has a "3. Analysis" section, your digest should have "# 3. Analysis". Preserve the paper's numbering and hierarchy.

4. **For each section, extract exhaustively**:
   - Every equation, rendered in LaTeX exactly as written. Do not simplify or re-derive.
   - Every numerical result with original precision, units, and rounding.
   - Every table reproduced in Markdown table format. (The downstream summary will re-render result tables as Markdown tables — never as images — so you must provide tables in parseable Markdown.)
   - Algorithm pseudocode if present.
   - Key definitions, theorems, propositions verbatim.
   - Hyperparameters, model names, dataset names, baselines — for BOTH proposed method AND every baseline individually. For EACH method (proposed AND each baseline), extract: architecture, key hyperparameters (lr, batch size, training steps/epochs, optimizer, scheduler, method-specific params), training condition (from scratch / finetune / pretrained checkpoint), and source (official repo / reimplemented / reported from paper). If any baseline HP is not reported, note "not reported" explicitly.
   - Narrative connective tissue: 1–2 sentences per subsection summarizing WHY the authors did this, not only WHAT they did. This helps the downstream agent write narrative-style H2/H3 sections.

5. **After all paper sections, append these fixed sections**:

# Figures and Tables index
- For each figure/table referenced in the main text, one line: `Fig/Tab N — short caption — what it shows — which paper section it belongs to`.
- This index lets the downstream agent decide which figure to embed in which section of its adaptive summary.

# Figure Candidates (mandatory trailing block)
- Emit 1 to 4 lines listing the figures most worth embedding in the summary, in **priority order** (most informative first). One candidate per line in this exact fixed pipe-delimited format:

CANDIDATE: Figure N | Section: <Method|Motivation|Observation|Setup|Result|Analysis|Discussion> | Reason: <one sentence why this figure belongs in that summary section>

- `N` is an integer that literally appears in the paper (e.g. `Figure 3`). Do NOT pick a table.
- `Section` is a single hint token picking which adaptive-summary section is the most natural home for this figure. Use only the seven tokens above.
- `Reason` is one sentence ending with a period, describing what the figure illustrates AND why it is useful in the chosen section.
- Prefer figures that illustrate method / mechanism / core intuition / key observation / schedule behavior. Avoid figures that only reproduce result numbers (result tables will be rendered as Markdown tables downstream, so a result-bar-chart figure is low value and usually not worth including).
- Do not duplicate the same figure number.
- If the paper contains no figure at all (text-only), emit exactly one line: `CANDIDATES: NONE — <one-sentence reason>`.
- These `CANDIDATE:` / `CANDIDATES: NONE` lines must be the LAST non-empty lines of your output, with nothing between them except newlines.

## Rules
- Be exhaustive on numbers and equations. The downstream agent cannot re-read the PDF.
- Do NOT add your own critique, opinion, or comparisons to other papers. (Critical reading is Claude's job downstream.)
- Do NOT summarize away numerical values. If the paper reports 47.3%, write 47.3%, not "about half".
- Do NOT reorganize or merge the paper's sections. Follow the paper's structure faithfully.
- Target length: 2500 to 6000 words of digest. Longer is fine if the paper is dense.
- Output plain Markdown only. No code fences around the whole response.
- **Figure Candidates block is mandatory**: the last non-empty lines of your output MUST be the `CANDIDATE:` lines (1–4) or the single `CANDIDATES: NONE` line, in the fixed format above. Do not wrap them in a section header, list, or code fence.
- Tables are NOT figures: never write `CANDIDATE: Table 3`. Only `Figure N` or `NONE` are valid.
"""


# -------- helpers ----------------------------------------------------------


def _log(msg: str) -> None:
    print(f"[gemini_digest] {msg}", file=sys.stderr, flush=True)


def _now_kst_iso() -> str:
    return _dt.datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S%z")


def _fail(code: int, msg: str) -> None:
    _log(f"FAIL ({code}): {msg}")
    sys.exit(code)


def _parse_frontmatter(raw_md_path: Path) -> dict:
    text = raw_md_path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        _fail(2, f"raw.md has no YAML frontmatter: {raw_md_path}")
    end = text.find("\n---", 3)
    if end < 0:
        _fail(2, f"raw.md frontmatter not closed: {raw_md_path}")
    fm_block = text[3:end].strip("\n")
    # Minimal, forgiving YAML parse: only the scalar keys we need. Avoids a
    # hard dependency on PyYAML in case the env ever drifts.
    meta: dict = {}
    for line in fm_block.splitlines():
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip()
        v = v.strip()
        # strip wrapping quotes
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
            v = v[1:-1]
        meta[k] = v
    return meta


def _slug_from_raw(raw_md_path: Path, meta: dict) -> str:
    slug = meta.get("slug")
    if slug:
        return slug
    # Fallback: <slug>.raw.md -> <slug>
    name = raw_md_path.name
    if name.endswith(".raw.md"):
        return name[: -len(".raw.md")]
    return raw_md_path.stem


def _download(url: str, dst: Path, timeout: int = 120) -> bool:
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "research_hub/gemini_digest.py (+paper-summarize)"
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        if not data or len(data) < 1024:
            _log(f"download too small ({len(data)} bytes): {url}")
            return False
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        _log(f"downloaded {len(data)} bytes from {url} -> {dst}")
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        _log(f"download failed: {url} ({e})")
        return False
    except Exception as e:  # noqa: BLE001
        _log(f"download unexpected error: {url} ({e})")
        return False


def _ensure_pdf(meta: dict, cache_path: Path, force: bool) -> Optional[Path]:
    if cache_path.exists() and cache_path.stat().st_size > 1024 and not force:
        _log(f"PDF cache hit: {cache_path}")
        return cache_path

    candidates: list[str] = []
    pdf_url = meta.get("pdf_url") or ""
    arxiv_id = meta.get("arxiv_id") or ""
    anthology_id = meta.get("anthology_id") or ""
    cvf_url = meta.get("cvf_url") or ""

    if pdf_url:
        candidates.append(pdf_url)
    if arxiv_id:
        candidates.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    if anthology_id:
        candidates.append(f"https://aclanthology.org/{anthology_id}.pdf")
    if cvf_url:
        # cvf_url may already be a PDF URL; if not, leave to manual resolution
        candidates.append(cvf_url)

    # dedup while preserving order
    seen = set()
    ordered = []
    for u in candidates:
        if u and u not in seen:
            seen.add(u)
            ordered.append(u)

    if not ordered:
        _log("no PDF URL candidates in raw.md frontmatter")
        return None

    for url in ordered:
        if _download(url, cache_path):
            return cache_path
    return None


def _parse_pdf(pdf_path: Path) -> str:
    try:
        import fitz  # type: ignore
    except Exception as e:  # noqa: BLE001
        _fail(4, f"pymupdf import failed: {e}")

    try:
        doc = fitz.open(str(pdf_path))
        pages = [p.get_text() for p in doc]
        doc.close()
    except Exception as e:  # noqa: BLE001
        _fail(4, f"pymupdf parse failed: {e}")
        return ""  # unreachable

    full_text = "\n\n".join(pages)
    if len(full_text) < MIN_FULLTEXT_CHARS:
        _fail(
            4,
            f"parsed full_text too short ({len(full_text)} < {MIN_FULLTEXT_CHARS})",
        )
    return full_text


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _digest_cache_valid(digest_path: Path, pdf_sha: str) -> bool:
    """Cache is valid only when BOTH source_pdf_sha256 AND prompt_version match.

    Bumping PROMPT_VERSION must force regeneration even if the PDF is unchanged.
    """
    if not digest_path.exists():
        return False
    try:
        text = digest_path.read_text(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        return False
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end < 0:
        return False
    fm = text[3:end]
    cached_sha: Optional[str] = None
    cached_prompt: Optional[str] = None
    for line in fm.splitlines():
        stripped = line.strip()
        if stripped.startswith("source_pdf_sha256:"):
            cached_sha = stripped.split(":", 1)[1].strip().strip("'\"")
        elif stripped.startswith("prompt_version:"):
            cached_prompt = stripped.split(":", 1)[1].strip().strip("'\"")
    if cached_sha != pdf_sha:
        return False
    if cached_prompt != PROMPT_VERSION:
        _log(
            f"digest cache prompt_version mismatch "
            f"(cached={cached_prompt}, current={PROMPT_VERSION}) → regenerate"
        )
        return False
    return True


def _call_gemini(full_text: str) -> str:
    try:
        proc = subprocess.run(
            ["gemini", "-m", GEMINI_MODEL, "-p", DIGEST_PROMPT, "-o", "text"],
            input=full_text,
            capture_output=True,
            text=True,
            timeout=GEMINI_TIMEOUT_SEC,
            check=False,
        )
    except FileNotFoundError:
        _fail(5, "gemini CLI not found in PATH")
    except subprocess.TimeoutExpired:
        _fail(5, f"gemini CLI timed out after {GEMINI_TIMEOUT_SEC}s")
    except Exception as e:  # noqa: BLE001
        _fail(5, f"gemini CLI invocation error: {e}")

    if proc.returncode != 0:
        err = (proc.stderr or "").strip()[:2000]
        _fail(5, f"gemini CLI returncode={proc.returncode}: {err}")

    out = (proc.stdout or "").strip()
    if len(out) < 200:
        _fail(5, f"gemini CLI output too short ({len(out)} chars)")
    return out


_SECTION_HINTS = {
    "method",
    "motivation",
    "observation",
    "setup",
    "result",
    "analysis",
    "discussion",
}


def _parse_figure_candidates(
    body: str,
) -> list[tuple[int, str, str]]:
    """Extract the trailing `CANDIDATE:` block from a gemini digest body.

    Returns a list of (figure_number, section_hint, reason) tuples, in the
    priority order Gemini emitted (most informative first). Max 4. Dedup by
    figure number (first occurrence wins). Returns an empty list when the
    digest contains `CANDIDATES: NONE` or when the block is missing /
    unparseable.

    Expected line format:
        CANDIDATE: Figure N | Section: <hint> | Reason: <one sentence>
    """
    # NONE shortcut — paper has no figure at all.
    if re.search(
        r"^\s*CANDIDATES?\s*:\s*NONE\b", body, re.MULTILINE | re.IGNORECASE
    ):
        return []

    pattern = re.compile(
        r"^\s*CANDIDATE\s*:\s*(?:Figure|Fig\.?)\s*(\d+)\s*"
        r"\|\s*Section\s*:\s*([A-Za-z][A-Za-z \-]*?)\s*"
        r"\|\s*Reason\s*:\s*(.+?)\s*$",
        re.MULTILINE | re.IGNORECASE,
    )

    out: list[tuple[int, str, str]] = []
    seen: set[int] = set()
    for m in pattern.finditer(body):
        try:
            n = int(m.group(1))
        except ValueError:
            continue
        if n in seen:
            continue
        hint_raw = m.group(2).strip().lower()
        # Normalize to one of _SECTION_HINTS or fall back to "method".
        hint = hint_raw if hint_raw in _SECTION_HINTS else "method"
        reason = m.group(3).strip()
        if "\n" in reason:
            reason = reason.split("\n", 1)[0].strip()
        out.append((n, hint, reason))
        seen.add(n)
        if len(out) >= 4:
            break

    if not out:
        _log("CANDIDATE block missing or unparseable in gemini output")
    return out


def _find_figure_caption_bbox(doc, fig_num: int):
    """Scan pages for a caption line of the form `Figure N[:.]`.

    Returns (page_index, caption_rect) for the first match, or (None, None).
    """
    try:
        import fitz  # type: ignore
    except Exception:  # noqa: BLE001
        return None, None

    pattern = re.compile(
        rf"^\s*(?:Figure|Fig\.?)\s*{fig_num}\b[\s:\.\u2014\u2013-]",
        re.IGNORECASE,
    )

    for page_idx in range(len(doc)):
        page = doc[page_idx]
        try:
            tdict = page.get_text("dict")
        except Exception as e:  # noqa: BLE001
            _log(f"page.get_text(dict) failed on page {page_idx}: {e}")
            continue
        for block in tdict.get("blocks", []):
            if block.get("type", 0) != 0:  # text blocks only
                continue
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if not spans:
                    continue
                line_text = "".join(s.get("text", "") for s in spans).strip()
                if not line_text:
                    continue
                if pattern.match(line_text):
                    # Use the line bbox (union of spans) for a tight anchor.
                    x0 = min(s["bbox"][0] for s in spans)
                    y0 = min(s["bbox"][1] for s in spans)
                    x1 = max(s["bbox"][2] for s in spans)
                    y1 = max(s["bbox"][3] for s in spans)
                    rect = fitz.Rect(x0, y0, x1, y1)
                    return page_idx, rect
    return None, None


def _refine_figure_region(page, region_rect):
    """Shrink `region_rect` to the union of image/drawing bboxes inside it.

    Falls back to the input rect if no images/drawings are found or if the
    refined rect is narrower than FIGURE_MIN_HEIGHT_FRAC of the page height.
    """
    try:
        import fitz  # type: ignore
    except Exception:  # noqa: BLE001
        return region_rect

    page_height = page.rect.height
    candidates = []

    # 1) Raster image blocks (type==1) from get_text("dict")
    try:
        tdict = page.get_text("dict")
        for block in tdict.get("blocks", []):
            if block.get("type", 0) == 1:
                bx = block.get("bbox")
                if bx:
                    r = fitz.Rect(bx)
                    if region_rect.intersects(r):
                        candidates.append(r & region_rect)
    except Exception as e:  # noqa: BLE001
        _log(f"image block scan failed: {e}")

    # 2) Vector drawings (figures often are matplotlib-style vectors)
    try:
        drawings = page.get_drawings()
        for d in drawings:
            bx = d.get("rect")
            if bx is None:
                continue
            r = fitz.Rect(bx)
            if region_rect.intersects(r):
                candidates.append(r & region_rect)
    except Exception as e:  # noqa: BLE001
        _log(f"get_drawings() failed: {e}")

    if not candidates:
        return region_rect

    union = candidates[0]
    for r in candidates[1:]:
        union = union | r

    if union.height < FIGURE_MIN_HEIGHT_FRAC * page_height:
        _log(
            f"refined bbox too small "
            f"(h={union.height:.1f} < {FIGURE_MIN_HEIGHT_FRAC*page_height:.1f}), "
            f"keeping raw region"
        )
        return region_rect
    return union


def _extract_figure_png(
    pdf_path: Path, fig_num: int, out_png: Path
) -> Optional[Path]:
    """Locate `Figure N` via caption search, crop the region above (or below)
    the caption, render to `out_png` at ~216 DPI, and return the path on
    success. Returns None on any failure — this is a best-effort extraction.
    """
    try:
        import fitz  # type: ignore
    except Exception as e:  # noqa: BLE001
        _log(f"pymupdf unavailable for figure extraction: {e}")
        return None

    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:  # noqa: BLE001
        _log(f"figure extract: fitz.open failed: {e}")
        return None

    try:
        _log(f"figure extract: searching for Figure {fig_num} (pymupdf {fitz.__version__})")
        page_idx, caption_rect = _find_figure_caption_bbox(doc, fig_num)
        if page_idx is None or caption_rect is None:
            _log(f"figure extract: caption for Figure {fig_num} not found")
            return None

        page = doc[page_idx]
        page_rect = page.rect
        _log(
            f"figure extract: found Figure {fig_num} caption on page "
            f"{page_idx + 1} at {tuple(round(v, 1) for v in caption_rect)}"
        )

        # Strategy 1: region above the caption
        above = fitz.Rect(
            page_rect.x0, page_rect.y0, page_rect.x1, caption_rect.y0
        )
        # Strategy 2: region below the caption (fallback)
        below = fitz.Rect(
            page_rect.x0, caption_rect.y1, page_rect.x1, page_rect.y1
        )

        crop_rect: Optional[object] = None
        if above.height >= FIGURE_MIN_HEIGHT_FRAC * page_rect.height:
            crop_rect = _refine_figure_region(page, above)
        if crop_rect is None or crop_rect.is_empty or crop_rect.height <= 0:
            if below.height >= FIGURE_MIN_HEIGHT_FRAC * page_rect.height:
                crop_rect = _refine_figure_region(page, below)
        if crop_rect is None or crop_rect.is_empty or crop_rect.height <= 0:
            _log("figure extract: both above/below regions empty, using full page")
            crop_rect = page_rect

        try:
            mat = fitz.Matrix(FIGURE_DPI_MATRIX, FIGURE_DPI_MATRIX)
            pix = page.get_pixmap(matrix=mat, clip=crop_rect, alpha=False)
        except Exception as e:  # noqa: BLE001
            _log(f"figure extract: get_pixmap failed ({e}); retrying full page")
            try:
                pix = page.get_pixmap(matrix=fitz.Matrix(FIGURE_DPI_MATRIX, FIGURE_DPI_MATRIX), alpha=False)
            except Exception as e2:  # noqa: BLE001
                _log(f"figure extract: full-page render also failed: {e2}")
                return None

        out_png.parent.mkdir(parents=True, exist_ok=True)
        try:
            pix.save(str(out_png))
        except Exception as e:  # noqa: BLE001
            _log(f"figure extract: pixmap.save failed: {e}")
            return None

        size = out_png.stat().st_size if out_png.exists() else 0
        if size < FIGURE_MIN_BYTES:
            _log(
                f"figure extract: rendered PNG too small ({size} bytes < "
                f"{FIGURE_MIN_BYTES}) → treating as failure"
            )
            try:
                out_png.unlink()
            except Exception:  # noqa: BLE001
                pass
            return None

        _log(
            f"figure extract: wrote {out_png} "
            f"({size} bytes, {pix.width}x{pix.height}px)"
        )
        return out_png
    finally:
        try:
            doc.close()
        except Exception:  # noqa: BLE001
            pass


def _write_digest(
    digest_path: Path,
    body: str,
    raw_md_path: Path,
    pdf_sha: str,
    meta: dict,
    figures: list[dict],
) -> None:
    """Write the digest markdown file.

    `figures` is a list of dicts (priority order, first = primary):
        [{label, path, section_hint, reason}, ...]
    May be empty when the paper has no figures or extraction failed for all.
    The first entry (if any) is also exposed as the `key_figure_*` shortcut
    for backward-compatible downstream readers.
    """
    digest_path.parent.mkdir(parents=True, exist_ok=True)

    def _yaml_str(v: Optional[str]) -> str:
        if v is None:
            return "null"
        # escape embedded double quotes
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'

    primary = figures[0] if figures else None

    fm_lines = [
        "---",
        f'source_raw: "{raw_md_path.as_posix()}"',
        f'source_pdf_sha256: "{pdf_sha}"',
        f'generated_at: "{_now_kst_iso()}"',
        f'model: "{GEMINI_MODEL}"',
        f'prompt_version: "{PROMPT_VERSION}"',
        f'slug: "{_slug_from_raw(raw_md_path, meta)}"',
        f'venue_class: "{meta.get("venue_class", "")}"',
        f'venue: "{meta.get("venue", "")}"',
        f'year: "{meta.get("year", "")}"',
        f"key_figure_label: {_yaml_str(primary['label'] if primary else None)}",
        f"key_figure_reason: {_yaml_str(primary['reason'] if primary else None)}",
        f"key_figure_path: {_yaml_str(primary['path'] if primary else None)}",
    ]
    if figures:
        fm_lines.append("figures:")
        for fig in figures:
            fm_lines.append(f'  - label: {_yaml_str(fig["label"])}')
            fm_lines.append(f'    path: {_yaml_str(fig["path"])}')
            fm_lines.append(f'    section_hint: {_yaml_str(fig["section_hint"])}')
            fm_lines.append(f'    reason: {_yaml_str(fig["reason"])}')
    else:
        fm_lines.append("figures: []")
    fm_lines.extend(["---", ""])
    digest_path.write_text("\n".join(fm_lines) + body + "\n", encoding="utf-8")


# -------- main -------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("raw_md", type=str, help="path to <slug>.raw.md")
    ap.add_argument(
        "--force",
        action="store_true",
        help="ignore PDF cache and digest cache",
    )
    args = ap.parse_args()

    raw_md_path = Path(args.raw_md).resolve()
    if not raw_md_path.exists():
        _fail(2, f"raw.md not found: {raw_md_path}")
    if not raw_md_path.name.endswith(".raw.md"):
        _log(f"warning: expected *.raw.md, got {raw_md_path.name}")

    try:
        meta = _parse_frontmatter(raw_md_path)
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        _fail(2, f"frontmatter parse failed: {e}")

    slug = _slug_from_raw(raw_md_path, meta)

    # Derive papers_root and venue/year part from the raw.md path.
    # raw_md_path is like: .../papers/metadata/<V>/<Y>/<slug>.raw.md
    # We find "metadata" in the path parts, then papers_root is its parent
    # and venue_year_part is everything between "metadata" and the filename.
    raw_parts = raw_md_path.parts
    try:
        meta_idx = raw_parts.index("metadata")
    except ValueError:
        _fail(2, f"raw.md path does not contain 'metadata/' component: {raw_md_path}")
    papers_root = Path(*raw_parts[:meta_idx])  # e.g. /home/.../papers
    venue_year_part = Path(*raw_parts[meta_idx + 1 : -1])  # e.g. ICLR/2025

    pdf_cache = papers_root / "digest" / venue_year_part / ".pdf_cache" / f"{slug}.pdf"
    digest_path = papers_root / "digest" / venue_year_part / f"{slug}.digest.md"

    pdf_path = _ensure_pdf(meta, pdf_cache, force=args.force)
    if pdf_path is None:
        _fail(3, "all PDF download candidates failed")

    pdf_sha = _sha256_file(pdf_path)

    if not args.force and _digest_cache_valid(digest_path, pdf_sha):
        _log(f"digest cache hit (same pdf sha): {digest_path}")
        print(str(digest_path))
        return 0

    _log(f"parsing PDF: {pdf_path}")
    full_text = _parse_pdf(pdf_path)
    _log(f"full_text chars={len(full_text)}")

    _log(
        f"calling gemini ({GEMINI_MODEL}, timeout={GEMINI_TIMEOUT_SEC}s, "
        f"prompt={PROMPT_VERSION})"
    )
    body = _call_gemini(full_text)
    _log(f"gemini digest chars={len(body)}")

    # --- Figure candidate selection + extraction (best-effort, non-fatal) ---
    candidates = _parse_figure_candidates(body)
    figures: list[dict] = []
    figure_cache_dir = (
        papers_root / "marp-summary" / venue_year_part / ".figure_cache"
    )

    if not candidates:
        _log("no figure candidates parsed (NONE or missing)")

    for fig_num, section_hint, reason in candidates:
        figure_png = figure_cache_dir / f"{slug}__fig{fig_num}.png"
        _log(
            f"gemini picked candidate Figure {fig_num} "
            f"(section_hint={section_hint}, reason={reason!r})"
        )
        extracted = _extract_figure_png(pdf_path, fig_num, figure_png)
        if extracted is None:
            _log(f"figure extraction failed for Figure {fig_num} → dropping from figures list")
            continue
        figures.append(
            {
                "label": f"Figure {fig_num}",
                # Relative path from the marp-summary/<V>/<Y>/ directory where
                # the final .md will live → .figure_cache/<slug>__fig<N>.png
                "path": f".figure_cache/{slug}__fig{fig_num}.png",
                "section_hint": section_hint,
                "reason": reason,
            }
        )

    _write_digest(
        digest_path,
        body,
        raw_md_path,
        pdf_sha,
        meta,
        figures=figures,
    )
    _log(f"wrote digest: {digest_path} (figures={len(figures)})")
    print(str(digest_path))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        traceback.print_exc(file=sys.stderr)
        _fail(6, f"unexpected error: {e}")
