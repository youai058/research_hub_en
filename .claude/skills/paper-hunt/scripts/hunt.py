"""Unified paper-hunt CLI entry point.

Scans 3 sources in one pass — OpenReview, ACL Anthology, arXiv — applies
`classify_route()` to every result, dedup by (normalized_title | arxiv_id |
openreview_id | anthology_id), and emits `raw.md` files under:

    papers/metadata/<Venue>/<Year>/<slug>.raw.md    (venue_class == "whitelist")
    papers/metadata/etc/<Year>/<slug>.raw.md        (venue_class == "etc")

This script uses **abstract + API metadata only**. Full-text fetch is not
the default path — it belongs to the paper-summarize skill. For the rare
"classification unclear / near-duplicate" cases, an optional helper is
exposed (see `optional_pdf_head()`) but must be invoked explicitly.

Usage:
    python3 hunt.py \
        --years 2026 2025 2024 \
        --venues-whitelist-all \
        --keywords "diffusion language model" "LLaDA" \
        [--sources openreview anthology arxiv] \
        [--root /home/irteam/sw/research_hub] \
        [--max-per-query 100] \
        [--max-per-venue-year 200] \
        [--dry-run]

Scan order (outer → inner): **year → source → venue**. The per-year source
order is fixed `openreview → anthology → arxiv` so that whitelist venue
labels are stamped first, and arXiv re-discoveries of the same paper are
dropped by the global dedup table. The year list preserves user-supplied
ordering (so `--years 2026 2025 2024` scans newest first); if `--years` is
omitted, it defaults to `[today.year, -1, -2]` in KST. The global dedup
table (normalized title + arxiv/openreview/anthology id) is preserved
**across year buckets** — a paper seen in the 2026 bucket is not
re-emitted in 2025/2024.

Every emission updates `papers/vector_db/manifest.json` with file hash + mtime +
normalized_title, and refreshes per-source cursors under `manifest.cursors`.
Dropping a result purely because it's not whitelist is forbidden — use
`venue_class: "etc"` instead.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

# Auto-load .env from research_hub root (research_hub/.env takes precedence
# over /home/irteam/sw/.env). Only sets keys not already in os.environ.
try:
    from dotenv import load_dotenv  # type: ignore
    for _env_candidate in (
        SCRIPT_DIR.parents[3] / ".env",   # research_hub/.env
        Path("/home/irteam/sw/.env"),     # legacy shared
    ):
        if _env_candidate.is_file():
            load_dotenv(_env_candidate, override=False)
except ImportError:
    pass

from classify_route import classify_route, CANONICAL, WHITELIST  # noqa: E402

KST = datetime.timezone(datetime.timedelta(hours=9))

# Gate for non-whitelist (venue_class == "etc") emissions from openreview
# and anthology scans. Flipped True by main() when --include-arxiv is passed;
# default False drops etc-classified results before they are written. The
# arXiv keyword source is gated one layer above — main() removes "arxiv"
# from args.sources when the flag is absent, so that source never runs.
_ALLOW_ETC = False

# Which whitelist venues publish on OpenReview as accepted papers, and how
# their venueid is formatted. Venues not in this map are handled by other
# sources (anthology for ACL/EMNLP, arXiv comment-based routing for AAAI).
# 404/nonexistent venueids are silently skipped by hunt_openreview().
OPENREVIEW_WHITELIST_VENUEID = {
    "ICLR": "ICLR.cc/{year}/Conference",
    "NeurIPS": "NeurIPS.cc/{year}/Conference",
    "ICML": "ICML.cc/{year}/Conference",
}

# ACL Anthology event slugs for whitelist NLP venues.
ANTHOLOGY_WHITELIST_EVENTS = {
    "ACL": "acl",
    "EMNLP": "emnlp",
    "NAACL": "naacl",
}

# Canonical order matching the 6 whitelist venues in user-facing order.
WHITELIST_ORDER = (
    "NeurIPS", "AAAI", "ICLR", "ICML",
    "ACL", "EMNLP",
)


def default_years() -> list[int]:
    """Default 3-year rolling window in KST, newest first."""
    y = datetime.datetime.now(KST).year
    return [y, y - 1, y - 2]


def build_openreview_venueids(years: list[int], explicit: list[str]) -> list[tuple[str, int]]:
    """Return [(venueid, year)] for the given year list, using the whitelist
    mapping. Also appends explicit user-provided venueids (parsed for year)."""
    out: list[tuple[str, int]] = []
    for year in years:
        for _venue, tpl in OPENREVIEW_WHITELIST_VENUEID.items():
            out.append((tpl.format(year=year), year))
    for vid in explicit or []:
        # crude year parse: "ICLR.cc/2026/Conference" → 2026
        m = re.search(r"/(\d{4})/", vid)
        if m:
            out.append((vid, int(m.group(1))))
        else:
            out.append((vid, 0))
    # dedup while preserving order
    seen: set[str] = set()
    uniq: list[tuple[str, int]] = []
    for vid, y in out:
        if vid in seen:
            continue
        seen.add(vid)
        uniq.append((vid, y))
    return uniq


# ------------------------------------------------------------------ utils

def norm_title(t: str) -> str:
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def slugify(t: str, maxlen: int = 60) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return (s[:maxlen] or "paper")


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def now_kst() -> str:
    return datetime.datetime.now(KST).isoformat(timespec="seconds")


def load_manifest(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {
        "version": 1,
        "embed_model": "BAAI/bge-m3",
        "last_update": None,
        "files": {},
        "cursors": {},
    }


def save_manifest(path: Path, m: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")


# ------------------------------------------------------------------ raw.md writer

def _presentation_rank(venue_content: str) -> int:
    """Return sort key from OpenReview content.venue field.

    Oral=0, Spotlight=1, Poster=2, Unknown=3.  Case-insensitive.
    ICML 2025 uses 'spotlightposter' — treated as spotlight (rank 1).
    """
    v = venue_content.lower()
    if "oral" in v:
        return 0
    if "spotlight" in v:
        return 1
    if "poster" in v:
        return 2
    return 3


def _presentation_type(venue_content: str) -> str:
    """Extract presentation type label from OpenReview content.venue field."""
    v = venue_content.lower()
    if "oral" in v:
        return "oral"
    if "spotlight" in v:
        return "spotlight"
    if "poster" in v:
        return "poster"
    return ""


def _route_path(root: Path, venue: str, year: int, venue_class: str, slug: str) -> Path:
    if venue_class == "whitelist":
        return root / "papers" / "metadata" / venue / str(year) / f"{slug}.raw.md"
    # etc — flat year-only layout, never a source-based subdir.
    return root / "papers" / "metadata" / "etc" / str(year) / f"{slug}.raw.md"


def write_raw(
    root: Path,
    *,
    venue: str,
    year: int,
    venue_class: str,
    title: str,
    authors: list[str],
    abstract: str,
    pdf_url: str,
    arxiv_id: str = "",
    openreview_id: str = "",
    anthology_id: str = "",
    published: str = "",
    categories: list[str] | None = None,
    keywords: list[str] | None = None,
    venue_source: str = "",
    presentation_type: str = "",
) -> Path:
    slug = slugify(title)
    out = _route_path(root, venue, year, venue_class, slug)
    if out.exists():
        return out
    out.parent.mkdir(parents=True, exist_ok=True)

    fm = {
        "title": title.strip().replace("\n", " "),
        "authors": authors or [],
        "venue": venue,
        "year": year,
        "venue_class": venue_class,
        "presentation_type": presentation_type or "",
        "arxiv_id": arxiv_id or "",
        "openreview_id": openreview_id or "",
        "anthology_id": anthology_id or "",
        "pdf_url": pdf_url or "",
        "published": published or "",
        "categories": categories or [],
        "keywords": keywords or [],
        "venue_source": venue_source or "",
        "hunter_fetched": now_kst(),
    }
    fm_yaml = "---\n"
    for k, v in fm.items():
        fm_yaml += f"{k}: {json.dumps(v, ensure_ascii=False)}\n"
    fm_yaml += "---\n\n"

    body = f"# {fm['title']}\n\n## Abstract\n{abstract.strip()}\n\n## Metadata\n"
    body += f"- venue: {venue}\n"
    body += f"- year: {year}\n"
    body += f"- authors: {', '.join(fm['authors'])}\n"
    body += f"- arxiv_id: {fm['arxiv_id']}\n"
    body += f"- openreview_id: {fm['openreview_id']}\n"
    body += f"- anthology_id: {fm['anthology_id']}\n"
    body += f"- pdf_url: {fm['pdf_url']}\n"
    body += f"- published: {fm['published']}\n"
    if keywords:
        body += f"- keywords: {', '.join(keywords)}\n"

    out.write_text(fm_yaml + body)
    return out


# ------------------------------------------------------------------ dedup state

class SeenKeys:
    def __init__(self, manifest: dict):
        self.titles: set[str] = set()
        self.arxiv: set[str] = set()
        self.openreview: set[str] = set()
        self.anthology: set[str] = set()
        for _, meta in manifest.get("files", {}).items():
            nt = meta.get("normalized_title")
            if nt:
                self.titles.add(nt)
            for field, bucket in (
                ("arxiv_id", self.arxiv),
                ("openreview_id", self.openreview),
                ("anthology_id", self.anthology),
            ):
                v = meta.get(field)
                if v:
                    bucket.add(v)

    def seen(self, *, title: str, arxiv_id: str = "", openreview_id: str = "",
             anthology_id: str = "") -> bool:
        if arxiv_id and arxiv_id in self.arxiv:
            return True
        if openreview_id and openreview_id in self.openreview:
            return True
        if anthology_id and anthology_id in self.anthology:
            return True
        nt = norm_title(title)
        if nt and nt in self.titles:
            return True
        return False

    def add(self, *, title: str, arxiv_id: str = "", openreview_id: str = "",
            anthology_id: str = "") -> None:
        self.titles.add(norm_title(title))
        if arxiv_id:
            self.arxiv.add(arxiv_id)
        if openreview_id:
            self.openreview.add(openreview_id)
        if anthology_id:
            self.anthology.add(anthology_id)


# ------------------------------------------------------------------ sources
# NOTE: each source is best-effort. Import lazily so a missing optional
# dependency (e.g. `openreview`) never breaks the other sources.

def hunt_arxiv_year(
    root: Path,
    year: int,
    keywords: list[str],
    max_per_query: int,
    max_per_venue_year: int,
    seen: SeenKeys,
    manifest: dict,
    per_venue_year_counts: dict[tuple[str, int], int],
) -> list[Path]:
    """arXiv search for a single year bucket (submittedDate range).

    Emits up to `max_per_query` per keyword, and enforces `max_per_venue_year`
    per (canonical venue, year) across the whole run via `per_venue_year_counts`.
    """
    try:
        import arxiv  # type: ignore
    except Exception as e:
        print(f"[arxiv] skip — import failed: {e}", file=sys.stderr)
        return []

    emitted: list[Path] = []
    client = arxiv.Client(page_size=20, delay_seconds=3, num_retries=5)
    for kw in keywords:
        q = (
            f'(ti:"{kw}" OR abs:"{kw}")'
            f' AND submittedDate:[{year}01010000 TO {year}12312359]'
        )
        print(f"[arxiv][{year}] {q}", flush=True)
        try:
            search = arxiv.Search(
                query=q,
                max_results=max_per_query,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )
            for r in client.results(search):
                aid = r.get_short_id().split("v")[0]
                if seen.seen(title=r.title, arxiv_id=aid):
                    continue
                venue, v_year, vclass = classify_route(r)
                # Prefer classifier year, else published year, else current bucket.
                final_year = v_year or (r.published.year if r.published else year)
                cap_key = (venue, final_year)
                if max_per_venue_year > 0 and per_venue_year_counts.get(cap_key, 0) >= max_per_venue_year:
                    continue
                path = write_raw(
                    root,
                    venue=venue,
                    year=final_year,
                    venue_class=vclass,
                    title=r.title,
                    authors=[a.name for a in r.authors],
                    abstract=r.summary,
                    pdf_url=r.pdf_url,
                    arxiv_id=aid,
                    published=r.published.strftime("%Y-%m-%d"),
                    categories=list(r.categories),
                    venue_source="arxiv-comment" if vclass == "whitelist" else "arxiv-only",
                )
                seen.add(title=r.title, arxiv_id=aid)
                per_venue_year_counts[cap_key] = per_venue_year_counts.get(cap_key, 0) + 1
                emitted.append(path)
                print(f"  + [{venue} {final_year} :: {vclass}] {r.title[:80]}", flush=True)
        except Exception as e:
            print(f"[arxiv] query failed: {type(e).__name__}: {e}", file=sys.stderr)
            if "429" in str(e):
                break

    manifest.setdefault("cursors", {})[f"arxiv:{year}:{','.join(keywords)}"] = {
        "last_run": now_kst(),
        "year": year,
    }
    return emitted


def hunt_openreview_year(
    root: Path,
    year: int,
    venue_ids: list[str],
    keywords: list[str],
    max_per_venue_year: int,
    seen: SeenKeys,
    manifest: dict,
    per_venue_year_counts: dict[tuple[str, int], int],
) -> list[Path]:
    """OpenReview fetch for a single year.

    `venue_ids` is the subset of venueids belonging to this year (the caller
    pre-filters). 404 / nonexistent venueids are silently skipped with a
    single stderr info line.
    """
    try:
        import openreview  # type: ignore
    except Exception as e:
        print(f"[openreview] skip — import failed: {e}", file=sys.stderr)
        return []

    emitted: list[Path] = []
    try:
        client = openreview.api.OpenReviewClient(
            baseurl="https://api2.openreview.net",
            username=os.environ.get("OPENREVIEW_USERNAME"),
            password=os.environ.get("OPENREVIEW_PASSWORD"),
        )
    except Exception as e:
        print(f"[openreview] client init failed: {e}", file=sys.stderr)
        return []

    for venue_id in venue_ids:
        print(f"[openreview][{year}] venueid={venue_id}", flush=True)
        try:
            notes = client.get_all_notes(content={"venueid": venue_id})
        except Exception as e:
            msg = str(e)
            if "404" in msg or "not found" in msg.lower() or "NotFoundError" in type(e).__name__:
                print(f"[openreview] skip — venueid not found: {venue_id}", file=sys.stderr)
            else:
                print(f"[openreview] get_all_notes failed ({venue_id}): {e}", file=sys.stderr)
            continue
        # Sort notes: oral → spotlight → poster so high-profile papers
        # are processed (and fill max_per_venue_year cap) first.
        def _note_sort_key(n):
            c = n.content or {}
            v = c.get("venue", {})
            if isinstance(v, dict):
                v = v.get("value", "")
            return _presentation_rank(str(v))
        notes.sort(key=_note_sort_key)
        ptype_counts = {}
        for n in notes:
            c0 = n.content or {}
            v0 = c0.get("venue", {})
            if isinstance(v0, dict):
                v0 = v0.get("value", "")
            pt = _presentation_type(str(v0))
            ptype_counts[pt or "unknown"] = ptype_counts.get(pt or "unknown", 0) + 1
        print(f"  . sorted {len(notes)} notes by presentation type: {ptype_counts}", flush=True)
        for n in notes:
            content = n.content or {}
            title = _val(content.get("title"))
            abstract = _val(content.get("abstract"))
            if not title or not abstract:
                continue
            # Keyword filtering on title + abstract (same semantics as
            # anthology and arXiv paths). Without this, a niche-topic hunt
            # on a large venue (e.g. ICLR with 2000+ accepted papers)
            # would emit max_per_venue_year random papers instead of
            # relevant ones.
            if keywords and not _kw_match(
                str(title) + " " + str(abstract), keywords
            ):
                continue

            forum_id = n.forum or n.id
            if seen.seen(title=str(title), openreview_id=forum_id):
                continue

            class Shim:
                comment = None
                journal_ref = None
                published = None
                openreview_venueid = venue_id

            class P:
                def __init__(self, yr):
                    self.year = yr

            shim = Shim()
            shim.published = P(year)
            venue, v_year, vclass = classify_route(shim)
            if v_year == 0:
                v_year = year
            if vclass == "etc" and not _ALLOW_ETC:
                continue

            cap_key = (venue, v_year)
            if max_per_venue_year > 0 and per_venue_year_counts.get(cap_key, 0) >= max_per_venue_year:
                # Can break out of venue loop once cap reached.
                print(f"  . cap reached for {venue} {v_year}", flush=True)
                break

            authors = _val(content.get("authors")) or []
            if isinstance(authors, str):
                authors = [authors]
            paper_keywords = _val(content.get("keywords")) or []
            if isinstance(paper_keywords, str):
                paper_keywords = [paper_keywords]
            pdf_field = _val(content.get("pdf"))
            if pdf_field and not str(pdf_field).startswith("http"):
                pdf_url = f"https://openreview.net{pdf_field}"
            else:
                pdf_url = pdf_field or f"https://openreview.net/forum?id={forum_id}"

            # Extract presentation type from content.venue field
            venue_field = content.get("venue", {})
            if isinstance(venue_field, dict):
                venue_field = venue_field.get("value", "")
            ptype = _presentation_type(str(venue_field))

            path = write_raw(
                root,
                venue=venue,
                year=v_year,
                venue_class=vclass,
                title=str(title),
                authors=authors,
                abstract=str(abstract),
                pdf_url=pdf_url,
                openreview_id=forum_id,
                keywords=paper_keywords,
                published=str(v_year),
                venue_source="openreview",
                presentation_type=ptype,
            )
            seen.add(title=str(title), openreview_id=forum_id)
            per_venue_year_counts[cap_key] = per_venue_year_counts.get(cap_key, 0) + 1
            emitted.append(path)
            ptype_tag = f" ({ptype})" if ptype else ""
            print(f"  + [{venue} {v_year} :: {vclass}]{ptype_tag} {str(title)[:80]}", flush=True)
            time.sleep(0.2)

        manifest.setdefault("cursors", {})[f"openreview:{venue_id}"] = {
            "last_run": now_kst(),
        }
    return emitted


def _kw_match(text: str, keywords: list[str]) -> bool:
    """Case-insensitive substring match — same semantics as arXiv path."""
    if not keywords:
        return True
    t = (text or "").lower()
    return any(kw.lower() in t for kw in keywords if kw)


class _Shim:
    """Minimal result-like object for classify_route()."""
    def __init__(
        self,
        *,
        comment: str | None = None,
        journal_ref: str | None = None,
        published_year: int | None = None,
        openreview_venueid: str | None = None,
        anthology_id: str | None = None,
    ) -> None:
        self.comment = comment
        self.journal_ref = journal_ref
        self.openreview_venueid = openreview_venueid
        self.anthology_id = anthology_id

        class _P:
            def __init__(self, y):
                self.year = y
        self.published = _P(published_year) if published_year else None


def hunt_anthology_year(
    root: Path,
    year: int,
    keywords: list[str],
    max_per_venue_year: int,
    seen: SeenKeys,
    manifest: dict,
    per_venue_year_counts: dict[tuple[str, int], int],
    anthology,
) -> list[Path]:
    """ACL Anthology scanner for a single year bucket.

    Uses the `acl-anthology` package (local XML data) instead of HTTP
    scraping.  Iterates collections → volumes → papers for each event
    in ANTHOLOGY_WHITELIST_EVENTS.
    """
    emitted: list[Path] = []
    for _canon, event in ANTHOLOGY_WHITELIST_EVENTS.items():
        coll_id = f"{year}.{event}"
        coll = anthology.collections.get(coll_id)
        if coll is None:
            print(f"[anthology][{year}] collection {coll_id} not found", file=sys.stderr)
            continue

        paper_count = 0
        for vol in coll.volumes():
            for paper in vol.papers():
                if paper.is_frontmatter:
                    continue
                paper_count += 1
                title = str(paper.title)
                anthology_id = paper.full_id

                if seen.seen(title=title, anthology_id=anthology_id):
                    continue

                shim = _Shim(anthology_id=anthology_id, published_year=year)
                venue, v_year, vclass = classify_route(shim)
                if vclass == "etc" and not _ALLOW_ETC:
                    continue

                cap_key = (venue, v_year)
                if per_venue_year_counts.get(cap_key, 0) >= max_per_venue_year:
                    continue

                abstract = str(paper.abstract) if paper.abstract else ""
                if keywords and not _kw_match(title + " " + abstract, keywords):
                    continue

                authors = [
                    f"{a.name.first} {a.name.last}".strip()
                    for a in (paper.authors or [])
                ]
                pdf_url = f"https://aclanthology.org/{anthology_id}.pdf"

                path = write_raw(
                    root,
                    venue=venue,
                    year=v_year,
                    venue_class=vclass,
                    title=title,
                    authors=authors,
                    abstract=abstract or "(abstract unavailable)",
                    pdf_url=pdf_url,
                    anthology_id=anthology_id,
                    published=str(v_year),
                    venue_source="anthology",
                )
                seen.add(title=title, anthology_id=anthology_id)
                per_venue_year_counts[cap_key] = per_venue_year_counts.get(cap_key, 0) + 1
                emitted.append(path)
                print(f"  + [{venue} {v_year} :: {vclass}] {title[:80]}", flush=True)

        print(f"[anthology][{year}] {event}-{year}: {paper_count} papers scanned", flush=True)
        manifest.setdefault("cursors", {})[f"anthology:{event}:{year}"] = {
            "last_run": now_kst(),
            "year": year,
        }
    return emitted


def _val(content_field):
    """OpenReview api2 wraps values as {'value': ...} dicts."""
    if isinstance(content_field, dict) and "value" in content_field:
        return content_field["value"]
    return content_field


# ------------------------------------------------------------------ main

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="paper-hunt CLI")
    ap.add_argument(
        "--root",
        default=None,
        help="research_hub root (default: auto-detect from script location)",
    )
    ap.add_argument("--venues", nargs="*", default=[],
                    help="Explicit OpenReview venueids (e.g. ICLR.cc/2026/Conference). "
                         "Merged with --venues-whitelist-all if set.")
    ap.add_argument("--venues-whitelist-all", action="store_true",
                    help="Target all 6 whitelist venues (NeurIPS/AAAI/ICLR/ICML/"
                         "ACL/EMNLP). Venues that don't use OpenReview fall "
                         "through to anthology/arXiv as appropriate.")
    ap.add_argument("--include-arxiv", action="store_true",
                    help="Opt-in: also run arXiv keyword source and keep "
                         "non-whitelist (venue_class='etc') results. Default "
                         "behaviour skips the arXiv source entirely and drops "
                         "any 'etc' emissions from openreview/anthology.")
    ap.add_argument("--keywords", nargs="*", default=[],
                    help="arXiv/Anthology keyword queries")
    ap.add_argument("--years", nargs="*", type=int, default=None,
                    help="Year buckets to scan, in scan-priority order "
                         "(newest first recommended). Defaults to "
                         "[today.year, today.year-1, today.year-2] in KST.")
    ap.add_argument("--date-from", default=None,
                    help="arXiv date lower bound YYYY-MM-DD. Ignored when --years is set "
                         "(year range takes precedence). Kept for backward compat.")
    ap.add_argument(
        "--sources",
        nargs="*",
        default=["openreview", "anthology", "arxiv"],
        choices=["openreview", "anthology", "arxiv"],
    )
    ap.add_argument("--max-per-query", type=int, default=100,
                    help="Upper bound for each arXiv keyword query per year.")
    ap.add_argument("--max-per-venue-year", type=int, default=0,
                    help="Upper bound for (canonical venue, year) total across sources. "
                         "0 = unlimited (collect all keyword-matching papers).")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    if args.root:
        root = Path(args.root).resolve()
    else:
        # paper-hunt/scripts/hunt.py → research_hub root is parents[4].
        root = Path(__file__).resolve().parents[4]

    # --include-arxiv: also pulls arXiv source and keeps non-whitelist (etc)
    # emissions. Default off — hunt stays strictly within the 6-venue
    # whitelist.
    global _ALLOW_ETC
    _ALLOW_ETC = bool(args.include_arxiv)
    if not args.include_arxiv and "arxiv" in args.sources:
        args.sources = [s for s in args.sources if s != "arxiv"]
        print(
            "[main] arXiv source skipped (pass --include-arxiv to enable "
            "arXiv keyword scan + etc routing)",
            file=sys.stderr,
        )

    # Year resolution: --years wins over --date-from. Preserve user ordering.
    if args.years:
        years: list[int] = list(args.years)
        if args.date_from:
            print("[main] --date-from ignored because --years is set", file=sys.stderr)
    else:
        years = default_years()
        if args.date_from:
            # Backward-compat: user only gave --date-from, no --years.
            # We still run in single-bucket legacy-ish mode: treat it as a
            # flat scan whose year is today's year (arxiv_year will apply
            # that year's submittedDate window — intentional tradeoff; the
            # new flow expects --years).
            print(
                "[main] --date-from supplied without --years; defaulting to "
                f"rolling window {years}",
                file=sys.stderr,
            )

    # Build OpenReview target list: user-explicit + whitelist-all expansion.
    explicit_venues = list(args.venues or [])
    if args.venues_whitelist_all:
        whitelist_pairs = build_openreview_venueids(years, explicit_venues)
    else:
        whitelist_pairs = build_openreview_venueids([], explicit_venues)  # just parse explicit

    manifest_path = root / "papers" / "vector_db" / "manifest.json"
    manifest = load_manifest(manifest_path)
    # SeenKeys is built from persisted manifest, then carried across all
    # year buckets. Do NOT reset per year — global dedup is a hard rule.
    seen = SeenKeys(manifest)
    per_venue_year_counts: dict[tuple[str, int], int] = {}

    # Lazy-init ACL Anthology package (local XML data, no HTTP).
    anthology_obj = None
    if "anthology" in args.sources:
        try:
            from acl_anthology import Anthology  # type: ignore
            anthology_obj = Anthology.from_repo()
            print("[anthology] init OK (local XML data)", file=sys.stderr)
        except Exception as e:
            print(f"[anthology] skip — init failed: {e}", file=sys.stderr)
            args.sources = [s for s in args.sources if s != "anthology"]

    all_emitted: list[Path] = []

    # --- year → source → venue scan loop ---
    # Fixed per-year source order: openreview → anthology → arxiv.
    # Rationale: OpenReview and Anthology stamp whitelist venue labels
    # authoritatively, so running them first populates the dedup table
    # before arXiv re-discovers the same paper via keyword search. arXiv
    # hits that match an already-seen arxiv_id / normalized title are then
    # dropped by SeenKeys.
    for year in years:
        year_start = len(all_emitted)
        print(f"\n=== [year {year}] ===", flush=True)

        if "openreview" in args.sources:
            year_venue_ids = [vid for (vid, y) in whitelist_pairs if y == year]
            if year_venue_ids:
                all_emitted += hunt_openreview_year(
                    root, year, year_venue_ids,
                    args.keywords or [],
                    args.max_per_venue_year,
                    seen, manifest, per_venue_year_counts,
                )

        if "anthology" in args.sources and anthology_obj is not None:
            all_emitted += hunt_anthology_year(
                root, year, args.keywords, args.max_per_venue_year,
                seen, manifest, per_venue_year_counts,
                anthology_obj,
            )

        if "arxiv" in args.sources and args.keywords:
            all_emitted += hunt_arxiv_year(
                root, year, args.keywords,
                args.max_per_query, args.max_per_venue_year,
                seen, manifest, per_venue_year_counts,
            )

        # Per-bucket summary line.
        bucket_paths = all_emitted[year_start:]
        wl = sum(1 for p in bucket_paths
                 if str(p.relative_to(root)).split("/")[2] != "etc")
        et = len(bucket_paths) - wl
        print(f"[year {year}] whitelist={wl}, etc={et}, bucket_total={len(bucket_paths)}",
              flush=True)

    # Update manifest with new files.
    for path in all_emitted:
        rel = str(path.relative_to(root))
        manifest["files"][rel] = {
            "sha256": sha256_file(path),
            "mtime": int(path.stat().st_mtime),
            "normalized_title": norm_title(_read_title(path)),
        }
    manifest["last_update"] = now_kst()

    if args.dry_run:
        print(f"[dry-run] would update manifest with {len(all_emitted)} new files")
    else:
        save_manifest(manifest_path, manifest)

    # Grand summary: whitelist/etc total + per-venue-year breakdown.
    # Path layout: papers/metadata/<Venue>/<Year>/ or papers/metadata/etc/<Year>/
    by_class = {"whitelist": 0, "etc": 0}
    for path in all_emitted:
        rel = str(path.relative_to(root))
        parts = rel.split("/")
        by_class["etc" if parts[2] == "etc" else "whitelist"] += 1

    per_venue_year_report = {
        f"{v} {y}": c for (v, y), c in sorted(per_venue_year_counts.items())
    }
    print(json.dumps(
        {
            "emitted": len(all_emitted),
            "whitelist": by_class["whitelist"],
            "etc": by_class["etc"],
            "years": years,
            "per_venue_year": per_venue_year_report,
            "manifest": str(manifest_path.relative_to(root)),
        },
        indent=2,
    ))
    return 0


def _read_title(path: Path) -> str:
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        return ""
    for line in text.splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"')
    return ""


if __name__ == "__main__":
    raise SystemExit(main())
