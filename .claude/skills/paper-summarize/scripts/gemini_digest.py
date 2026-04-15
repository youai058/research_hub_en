#!/usr/bin/env python3
"""
gemini_digest.py — Stage 1 of the 2-stage paper summarization pipeline.

Reads a paper-hunter raw.md, downloads the full PDF via a 4-way fallback,
parses it with pymupdf, and asks the Gemini CLI (gemini-3-pro-preview) to produce a
dense, faithful content digest. The digest is written next to the raw.md under
a hidden `.gemini_digest/` subdirectory so the Claude-side paper-summarizer
agent can finalize the 5-part Marp summary without re-reading the PDF.

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

PROMPT_VERSION = "v2"
GEMINI_MODEL = "gemini-3-pro-preview"
GEMINI_TIMEOUT_SEC = 600
MIN_FULLTEXT_CHARS = 3000
KST = _dt.timezone(_dt.timedelta(hours=9))
FIGURE_DPI_MATRIX = 3  # ~216 DPI at fitz default 72 DPI
FIGURE_MIN_BYTES = 10 * 1024  # 10KB sanity threshold
FIGURE_MIN_HEIGHT_FRAC = 0.10  # refined bbox must be >=10% of page height

DIGEST_PROMPT = """You are extracting a dense, faithful content digest of a research paper for a downstream critical-reading agent. The paper's full text has been provided above via stdin.

Produce a Markdown digest with these sections, in this order:

# Metadata
- Title, authors, venue, year (verbatim from the paper).

# Claims (verbatim)
- Bullet list of the paper's explicit claims. Quote the author's own wording using blockquotes. Do NOT paraphrase. Do NOT add interpretation.

# Methodology
- Core idea in one sentence, then the technical details.
- Every equation that appears in the main text, rendered in LaTeX exactly as written. Do not simplify or re-derive.
- Algorithm pseudocode if present.

# Experimental Setup
- Models (names + sizes), datasets (names + splits), baselines, hyperparameters (lr, batch, steps, optimizer, schedule), seeds / number of runs, hardware, training/inference budget. One field per line, original values only.

# Results
- Every numerical result reported in the main tables and main text. Preserve original precision, units, and rounding. Organize as a table when possible.
- Statistical significance reporting (error bars, p-values, confidence intervals) if any.
- Report the exact comparison (baseline -> proposed method -> delta).

# Ablations
- Each ablation study the paper runs, with the variable changed and the numerical effect.

# Limitations stated by authors
- Only what the authors explicitly acknowledge. Do not invent limitations.

# Figures and Tables index
- For each figure/table referenced in the main text, one line: `Fig/Tab N — short caption — what it shows`.

# Keywords
- 10 to 15 keywords or key phrases the paper itself uses.

# Key Figure (mandatory trailing block)
- After the Keywords section, emit exactly two lines in this exact fixed format, with no surrounding markdown, no bullets, no code fence:

KEY_FIGURE: Figure N
KEY_FIGURE_REASON: <one sentence why this figure is the single most informative for a reader>

- `N` is an integer figure number that literally appears in the paper (e.g. `Figure 3`). Do NOT pick a table — only Figure. If the paper has only `Figure 1`, pick `1`.
- If the paper contains no figure at all (text-only), emit `KEY_FIGURE: NONE` and a one-sentence reason explaining why no figure is available.
- The reason must be a single sentence on one line.

Rules:
- Be exhaustive on numbers and equations. The downstream agent cannot re-read the PDF.
- Do NOT add your own critique, opinion, or comparisons to other papers.
- Do NOT summarize away numerical values. If the paper reports 47.3%, write 47.3%, not "about half".
- If a section is absent in the paper, write "(not reported in paper)".
- Target length: 2000 to 5000 words of digest. Longer is fine if the paper is dense.
- Output plain Markdown only. No code fences around the whole response.
- **KEY_FIGURE block is mandatory**: the last two non-empty lines of your output MUST be the `KEY_FIGURE:` and `KEY_FIGURE_REASON:` lines, in that order, in the fixed format above. Do not wrap them in a section header, list, or code fence.
- Tables are NOT figures: never write `KEY_FIGURE: Table 3`. Only `Figure N` or `NONE` are valid.
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


def _parse_key_figure(body: str) -> Tuple[Optional[int], Optional[str]]:
    """Extract KEY_FIGURE trailing block from a gemini digest body.

    Returns (figure_number_or_None, reason_or_None). figure_number is an int
    when Gemini picked `Figure N`, None when Gemini emitted `NONE` or when the
    block is missing/malformed.
    """
    fig_num: Optional[int] = None
    reason: Optional[str] = None

    # Match `KEY_FIGURE: Figure 3` (case-insensitive, tolerant of `Fig.`)
    m_fig = re.search(
        r"^\s*KEY_FIGURE\s*:\s*(?:Figure|Fig\.?)\s*(\d+)\s*$",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    if m_fig:
        try:
            fig_num = int(m_fig.group(1))
        except ValueError:
            fig_num = None
    else:
        # Accept `KEY_FIGURE: NONE` as explicit no-figure signal.
        m_none = re.search(
            r"^\s*KEY_FIGURE\s*:\s*NONE\s*$", body, re.MULTILINE | re.IGNORECASE
        )
        if not m_none:
            _log("KEY_FIGURE block missing or unparseable in gemini output")

    m_reason = re.search(
        r"^\s*KEY_FIGURE_REASON\s*:\s*(.+?)\s*$", body, re.MULTILINE | re.IGNORECASE
    )
    if m_reason:
        reason = m_reason.group(1).strip()
        # Strip any trailing sentence bleed (keep single line)
        if "\n" in reason:
            reason = reason.split("\n", 1)[0].strip()
    return fig_num, reason


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
    key_figure_label: Optional[str],
    key_figure_reason: Optional[str],
    key_figure_path: Optional[str],
) -> None:
    digest_path.parent.mkdir(parents=True, exist_ok=True)

    def _yaml_str(v: Optional[str]) -> str:
        if v is None:
            return "null"
        # escape embedded double quotes
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'

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
        f"key_figure_label: {_yaml_str(key_figure_label)}",
        f"key_figure_reason: {_yaml_str(key_figure_reason)}",
        f"key_figure_path: {_yaml_str(key_figure_path)}",
        "---",
        "",
    ]
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
    base_dir = raw_md_path.parent
    pdf_cache = base_dir / ".pdf_cache" / f"{slug}.pdf"
    digest_dir = base_dir / ".gemini_digest"
    digest_path = digest_dir / f"{slug}.digest.md"

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

    # --- Key figure selection + extraction (best-effort, non-fatal) ---
    fig_num, fig_reason = _parse_key_figure(body)
    key_figure_label: Optional[str] = None
    key_figure_reason: Optional[str] = fig_reason
    key_figure_rel_path: Optional[str] = None

    if fig_num is not None:
        key_figure_label = f"Figure {fig_num}"
        figure_cache_dir = base_dir / ".figure_cache"
        figure_png = figure_cache_dir / f"{slug}.png"
        _log(
            f"gemini picked KEY_FIGURE=Figure {fig_num} "
            f"(reason={fig_reason!r})"
        )
        extracted = _extract_figure_png(pdf_path, fig_num, figure_png)
        if extracted is not None:
            # Path relative to raw.md directory, POSIX separators for Marp.
            try:
                rel = extracted.resolve().relative_to(base_dir.resolve())
                key_figure_rel_path = rel.as_posix()
            except Exception:  # noqa: BLE001
                key_figure_rel_path = f".figure_cache/{slug}.png"
        else:
            _log("figure extraction failed → key_figure_path=null")
    else:
        _log("no KEY_FIGURE picked (NONE or missing)")

    _write_digest(
        digest_path,
        body,
        raw_md_path,
        pdf_sha,
        meta,
        key_figure_label=key_figure_label,
        key_figure_reason=key_figure_reason,
        key_figure_path=key_figure_rel_path,
    )
    _log(f"wrote digest: {digest_path}")
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
