"""Unified paper-hunt CLI entry point.

Scans 3 sources in one pass — OpenReview, ACL Anthology, arXiv — applies
`classify_route()` to every result, dedup by (normalized_title | arxiv_id |
openreview_id | anthology_id), and emits `raw.md` files under:

    papers/<Venue>/<Year>/<slug>.raw.md    (venue_class == "whitelist")
    papers/etc/<Year>/<slug>.raw.md        (venue_class == "etc")

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

Every emission updates `papers/rag/manifest.json` with file hash + mtime +
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

def _route_path(root: Path, venue: str, year: int, venue_class: str, slug: str) -> Path:
    if venue_class == "whitelist":
        return root / "papers" / venue / str(year) / f"{slug}.raw.md"
    # etc — flat year-only layout, never a source-based subdir.
    return root / "papers" / "etc" / str(year) / f"{slug}.raw.md"


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
                if per_venue_year_counts.get(cap_key, 0) >= max_per_venue_year:
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
        for n in notes:
            content = n.content or {}
            title = _val(content.get("title"))
            abstract = _val(content.get("abstract"))
            if not title or not abstract:
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
            if per_venue_year_counts.get(cap_key, 0) >= max_per_venue_year:
                # Can break out of venue loop once cap reached.
                print(f"  . cap reached for {venue} {v_year}", flush=True)
                break

            authors = _val(content.get("authors")) or []
            if isinstance(authors, str):
                authors = [authors]
            keywords = _val(content.get("keywords")) or []
            if isinstance(keywords, str):
                keywords = [keywords]
            pdf_field = _val(content.get("pdf"))
            if pdf_field and not str(pdf_field).startswith("http"):
                pdf_url = f"https://openreview.net{pdf_field}"
            else:
                pdf_url = pdf_field or f"https://openreview.net/forum?id={forum_id}"

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
                keywords=keywords,
                published=str(v_year),
                venue_source="openreview",
            )
            seen.add(title=str(title), openreview_id=forum_id)
            per_venue_year_counts[cap_key] = per_venue_year_counts.get(cap_key, 0) + 1
            emitted.append(path)
            print(f"  + [{venue} {v_year} :: {vclass}] {str(title)[:80]}", flush=True)
            time.sleep(0.2)

        manifest.setdefault("cursors", {})[f"openreview:{venue_id}"] = {
            "last_run": now_kst(),
        }
    return emitted


# ------------------------------------------------------------------ HTTP utilities
# Shared across anthology source (+ any future scraper). Uses `requests`
# if available, else falls back to `urllib.request`. Every GET sets a
# User-Agent because aclanthology.org blocks empty UAs.

_UA = "research-hub-paperhunt/1.0"


def _http_get(url: str, *, timeout: int = 30) -> str | None:
    """Fetch `url` → text body. Returns None on 404 (silent), raises on
    unrecoverable failure. Handles 429 with one retry after 30s. Uses
    exponential backoff (3 attempts) for transient network errors."""
    headers = {"User-Agent": _UA}
    try:
        import requests  # type: ignore
        _backend = "requests"
    except Exception:
        requests = None  # type: ignore
        _backend = "urllib"

    last_err: Exception | None = None
    for attempt in range(3):
        try:
            if _backend == "requests":
                resp = requests.get(url, headers=headers, timeout=timeout)
                code = resp.status_code
                if code == 404:
                    return None
                if code == 429:
                    print(f"[http] 429 {url}; sleeping 30s", file=sys.stderr)
                    time.sleep(30)
                    resp = requests.get(url, headers=headers, timeout=timeout)
                    if resp.status_code == 404:
                        return None
                    resp.raise_for_status()
                    return resp.text
                resp.raise_for_status()
                return resp.text
            else:
                import urllib.request
                import urllib.error
                req = urllib.request.Request(url, headers=headers)
                try:
                    with urllib.request.urlopen(req, timeout=timeout) as r:
                        return r.read().decode("utf-8", errors="replace")
                except urllib.error.HTTPError as he:
                    if he.code == 404:
                        return None
                    if he.code == 429:
                        print(f"[http] 429 {url}; sleeping 30s", file=sys.stderr)
                        time.sleep(30)
                        with urllib.request.urlopen(req, timeout=timeout) as r:
                            return r.read().decode("utf-8", errors="replace")
                    raise
        except Exception as e:  # network-level
            last_err = e
            wait = 2 ** attempt
            print(
                f"[http] attempt {attempt + 1}/3 failed ({type(e).__name__}: {e}); "
                f"retry in {wait}s",
                file=sys.stderr,
            )
            time.sleep(wait)
    raise RuntimeError(f"GET failed after 3 attempts: {url} :: {last_err}")


def _try_bs(html: str):
    """Return BeautifulSoup(html) if bs4 available, else None."""
    try:
        from bs4 import BeautifulSoup  # type: ignore
        return BeautifulSoup(html, "html.parser")
    except Exception:
        return None


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


# ------------------------------------------------------------------ ACL Anthology

# Anthology listing-page anchors look like:
#   /2024.acl-long.123/           (main long)
#   /2024.findings-acl.45/        (findings)
#   /2024.emnlp-main.7/
#   /2024.naacl-short.12/
# Volume index anchors end in `.0/` and are skipped.
_ANTH_ID_RE = re.compile(
    r"^/((?P<yr>\d{4})\.(?P<track>(findings-)?(acl|emnlp|naacl))"
    r"-(?P<kind>long|short|main|demos|srw|tutorials|industry|system)\.(?P<num>\d+))/?$"
)


def _anth_fetch_listing(year: int, event: str) -> list[tuple[str, str]]:
    """Return [(anthology_id, title)] parsed from the event page.

    `event` ∈ {'acl', 'emnlp', 'naacl'}. Silently returns [] on 404 (event
    did not happen that year, e.g. NAACL has gap years).
    """
    url = f"https://aclanthology.org/events/{event}-{year}/"
    print(f"[anthology][{year}] fetch {url}", file=sys.stderr)
    html = _http_get(url, timeout=30)
    if html is None:
        print(f"[anthology][{year}] 404 {event}-{year}", file=sys.stderr)
        return []
    soup = _try_bs(html)
    results: list[tuple[str, str]] = []

    if soup is not None:
        # Every paper has an <a href="/YYYY.track-kind.N/"> with the title as text.
        for a in soup.find_all("a", href=True):
            href = a["href"]
            m = _ANTH_ID_RE.match(href)
            if not m:
                continue
            if int(m.group("yr")) != year:
                continue
            if m.group("num") == "0":
                continue  # volume index
            title = a.get_text(" ", strip=True)
            if not title or title.lower() in ("pdf", "bib", "abs"):
                continue
            aid = m.group(1)
            results.append((aid, title))
    else:
        # Fallback: regex over raw HTML.
        pat = re.compile(
            r'href="(/(\d{4}\.(?:findings-)?(?:acl|emnlp|naacl)'
            r'-(?:long|short|main|demos|srw|tutorials|industry|system)\.\d+)/?)">'
            r'([^<]{4,300})</a>'
        )
        for m in pat.finditer(html):
            aid_path = m.group(1)
            aid = aid_path.strip("/")
            inner = _ANTH_ID_RE.match("/" + aid + "/")
            if not inner:
                continue
            if int(inner.group("yr")) != year or inner.group("num") == "0":
                continue
            title = m.group(3).strip()
            if not title:
                continue
            results.append((aid, title))

    # Dedup by anthology_id while preserving order.
    uniq_seen: set[str] = set()
    uniq: list[tuple[str, str]] = []
    for aid, title in results:
        if aid in uniq_seen:
            continue
        uniq_seen.add(aid)
        uniq.append((aid, title))
    return uniq


def _anth_fetch_detail(anthology_id: str) -> dict:
    """Fetch a paper detail page → {authors, abstract, pdf_url}.

    Returns empty-string fields on failure so callers can still emit with
    partial info.
    """
    url = f"https://aclanthology.org/{anthology_id}/"
    out = {"authors": [], "abstract": "", "pdf_url": f"https://aclanthology.org/{anthology_id}.pdf"}
    try:
        html = _http_get(url, timeout=30)
    except Exception as e:
        print(f"[anthology] detail fetch failed {anthology_id}: {e}", file=sys.stderr)
        return out
    if html is None:
        return out
    soup = _try_bs(html)
    if soup is None:
        return out
    try:
        lead = soup.find("p", class_="lead")
        if lead:
            txt = lead.get_text(" ", strip=True)
            # Authors are comma-separated inside the lead paragraph.
            out["authors"] = [a.strip() for a in re.split(r",\s*", txt) if a.strip()]
        abst = soup.find("div", class_="acl-abstract")
        if abst:
            atxt = abst.get_text(" ", strip=True)
            # Strip literal "Abstract" prefix when present.
            atxt = re.sub(r"^Abstract\s*", "", atxt)
            out["abstract"] = atxt
    except Exception as e:  # pragma: no cover
        print(f"[anthology] detail parse failed {anthology_id}: {e}", file=sys.stderr)
    return out


def _anth_venue_label(anthology_id: str) -> tuple[str, str]:
    """Map anthology_id → (display_venue_label, canonical_event).

    - `2024.acl-long.123` → ("ACL", "acl")  [main → whitelist via classify_route]
    - `2024.findings-emnlp.7` → ("EMNLP Findings", "emnlp")  [→ etc]
    """
    m = re.match(
        r"^(\d{4})\.(findings-)?(acl|emnlp|naacl)-",
        anthology_id,
        re.IGNORECASE,
    )
    if not m:
        return ("ACL Anthology", "acl")
    is_findings = bool(m.group(2))
    ev = m.group(3).lower()
    canon = {"acl": "ACL", "emnlp": "EMNLP", "naacl": "NAACL"}[ev]
    if is_findings:
        return (f"{canon} Findings", ev)
    return (canon, ev)


def hunt_anthology_year(
    root: Path,
    year: int,
    keywords: list[str],
    max_per_venue_year: int,
    seen: SeenKeys,
    manifest: dict,
    per_venue_year_counts: dict[tuple[str, int], int],
) -> list[Path]:
    """ACL Anthology scanner for a single year bucket.

    Scans ACL / EMNLP / NAACL event pages, enumerates every anthology_id
    (main proceedings + Findings + workshops rolled in), filters by keyword
    match on title (cheap) and then title+abstract after detail fetch (full).
    Emits via the shared write_raw / classify_route path — main proceedings
    route to whitelist, Findings/workshops to etc.
    """
    emitted: list[Path] = []
    for _canon, event in ANTHOLOGY_WHITELIST_EVENTS.items():
        try:
            listing = _anth_fetch_listing(year, event)
        except Exception as e:
            print(
                f"[anthology][{year}] {event} listing failed: {type(e).__name__}: {e}",
                file=sys.stderr,
            )
            continue
        print(f"[anthology][{year}] {event}-{year}: {len(listing)} entries", flush=True)

        for anthology_id, title in listing:
            venue_label, _ev = _anth_venue_label(anthology_id)

            # No title-only pre-filter: user requires keyword matching to cover
            # title AND abstract on every source (2026-04-15 lesson). We still
            # short-circuit via the `per_venue_year_counts` cap below so detail
            # fetches halt once max_per_venue_year hits land in a bucket.
            if seen.seen(title=title, anthology_id=anthology_id):
                continue

            # classify_route decides whitelist vs etc from the anthology_id.
            shim = _Shim(anthology_id=anthology_id, published_year=year)
            venue, v_year, vclass = classify_route(shim)
            if vclass == "etc" and not _ALLOW_ETC:
                continue
            if vclass != "whitelist":
                # findings / workshops → keep the pretty label
                venue = venue_label
                v_year = year

            cap_key = (venue, v_year)
            if per_venue_year_counts.get(cap_key, 0) >= max_per_venue_year:
                # Skip ahead: don't pay detail-fetch cost once this bucket
                # is capped. The remaining entries may include other venues
                # (findings vs main share the same event page), so we
                # `continue` rather than `break`.
                continue

            # Detail fetch for abstract + authors.
            detail = _anth_fetch_detail(anthology_id)
            time.sleep(0.3)

            # Now run the full keyword filter (title + abstract).
            if keywords and not _kw_match(
                (title or "") + " " + (detail["abstract"] or ""),
                keywords,
            ):
                continue

            path = write_raw(
                root,
                venue=venue,
                year=v_year,
                venue_class=vclass,
                title=title,
                authors=detail["authors"],
                abstract=detail["abstract"] or "(abstract unavailable)",
                pdf_url=detail["pdf_url"],
                anthology_id=anthology_id,
                published=str(v_year),
                venue_source="anthology",
            )
            seen.add(title=title, anthology_id=anthology_id)
            per_venue_year_counts[cap_key] = per_venue_year_counts.get(cap_key, 0) + 1
            emitted.append(path)
            print(f"  + [{venue} {v_year} :: {vclass}] {title[:80]}", flush=True)

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
    ap.add_argument("--max-per-venue-year", type=int, default=200,
                    help="Upper bound for (canonical venue, year) total across sources.")
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

    manifest_path = root / "papers" / "rag" / "manifest.json"
    manifest = load_manifest(manifest_path)
    # SeenKeys is built from persisted manifest, then carried across all
    # year buckets. Do NOT reset per year — global dedup is a hard rule.
    seen = SeenKeys(manifest)
    per_venue_year_counts: dict[tuple[str, int], int] = {}

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
                    args.max_per_venue_year,
                    seen, manifest, per_venue_year_counts,
                )

        if "anthology" in args.sources:
            all_emitted += hunt_anthology_year(
                root, year, args.keywords, args.max_per_venue_year,
                seen, manifest, per_venue_year_counts,
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
                 if str(p.relative_to(root)).split("/")[1] != "etc")
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
    by_class = {"whitelist": 0, "etc": 0}
    for path in all_emitted:
        rel = str(path.relative_to(root))
        parts = rel.split("/")
        by_class["etc" if parts[1] == "etc" else "whitelist"] += 1

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
