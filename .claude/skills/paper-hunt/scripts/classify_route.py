"""Routing helper for paper-hunt.

Pure-function `classify_route()` — given a paper object (with `comment`,
`journal_ref`, `published`, optionally `venueid`), return
`(venue, year, venue_class)` where `venue_class ∈ {"whitelist", "etc"}`.

This is NOT a gate. Every paper returned by any source (official whitelist
venues, arXiv keyword queries, reference-chasing, web search) goes through
this to decide storage path. `etc` is a normal output path, never a drop.

Importable: `from classify_route import classify_route, WHITELIST, VENUE_PAT`.
"""
from __future__ import annotations

import re
from typing import Any

VENUE_PAT = re.compile(
    r"\b(NeurIPS|NIPS|AAAI|ICLR|ICML|IJCAI|ACL|EMNLP|NAACL)"
    r"\s*[\-:]?\s*(20\d{2})\b",
    re.IGNORECASE,
)

WHITELIST = {
    "NEURIPS",
    "AAAI",
    "ICLR",
    "ICML",
    "ACL",
    "EMNLP",
}

CANONICAL = {
    "NEURIPS": "NeurIPS",
    "AAAI": "AAAI",
    "ICLR": "ICLR",
    "ICML": "ICML",
    "IJCAI": "IJCAI",
    "ACL": "ACL",
    "EMNLP": "EMNLP",
    "NAACL": "NAACL",
}

# OpenReview venueid matcher (whitelist OR venues only).
OPENREVIEW_VENUEID_PAT = re.compile(
    r"^(NeurIPS|ICLR|ICML)\.cc/(\d{4})/Conference$",
    re.IGNORECASE,
)


def classify_route(result: Any) -> tuple[str, int, str]:
    """Classify a paper result into (venue, year, venue_class).

    `result` can be any object exposing some of these attributes / keys:
      - comment            (arxiv.Result.comment)
      - journal_ref        (arxiv.Result.journal_ref)
      - published          (arxiv.Result.published, has .year)
      - openreview_venueid (optional, str — e.g. "ICLR.cc/2026/Conference")
      - anthology_id       (optional, str — e.g. "2025.findings-emnlp.123")

    Rules:
      1. If `openreview_venueid` matches an accepted whitelist venue → whitelist.
      2. Else if `comment` or `journal_ref` contains a whitelist venue token
         followed by a 4-digit year → whitelist.
      3. Else if `anthology_id` starts with `YYYY.<acl|emnlp|naacl>-` (main
         proceedings, NOT `findings-*`) → whitelist.
      4. Otherwise → etc. Venue label is `journal_ref` or "arXiv" verbatim;
         year is from `published` or 0.
    """
    # 1. OpenReview venueid (most reliable).
    or_venueid = _get(result, "openreview_venueid")
    if or_venueid:
        m = OPENREVIEW_VENUEID_PAT.match(str(or_venueid))
        if m:
            canonical = CANONICAL[m.group(1).upper()]
            return canonical, int(m.group(2)), "whitelist"

    # 2. arXiv comment / journal_ref pattern.
    comment = _get(result, "comment") or ""
    journal_ref = _get(result, "journal_ref") or ""
    haystack = " ".join(filter(None, [comment, journal_ref]))
    detected_venue: tuple[str, int] | None = None
    if haystack:
        m = VENUE_PAT.search(haystack)
        if m:
            v = m.group(1).upper().replace("NIPS", "NEURIPS")
            if v in WHITELIST:
                return CANONICAL[v], int(m.group(2)), "whitelist"
            if v in CANONICAL:
                # Recognised venue but not whitelisted — preserve the label
                # for etc routing so the frontmatter shows the original
                # venue name instead of "arXiv".
                detected_venue = (f"{CANONICAL[v]} {m.group(2)}", int(m.group(2)))

    # 3. ACL Anthology main proceedings (NOT findings).
    anthology_id = _get(result, "anthology_id") or ""
    if anthology_id:
        m = re.match(
            r"^(\d{4})\.(acl|emnlp|naacl)-(long|short|main)\b",
            anthology_id,
            re.IGNORECASE,
        )
        if m:
            year = int(m.group(1))
            v = m.group(2).upper()
            cls = "whitelist" if v in WHITELIST else "etc"
            return CANONICAL[v], year, cls

    # 4. Fallback — route to etc/ with original venue string preserved.
    # If rule #2 recognised a non-whitelisted venue, honour that label
    # instead of falling back to "arXiv".
    if detected_venue is not None:
        return detected_venue[0], detected_venue[1], "etc"
    venue_label = (journal_ref or "arXiv").strip() or "arXiv"
    published = _get(result, "published")
    year = 0
    if published is not None:
        year = int(getattr(published, "year", 0) or 0)
    if not year:
        # Try to parse a year out of journal_ref as last resort.
        m = re.search(r"\b(20\d{2})\b", venue_label)
        if m:
            year = int(m.group(1))
    return venue_label, year, "etc"


def _get(obj: Any, key: str) -> Any:
    """Attribute-or-dict accessor (safe for arxiv.Result and plain dicts)."""
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


if __name__ == "__main__":
    # Smoke test.
    class R:
        def __init__(self, **kw):
            for k, v in kw.items():
                setattr(self, k, v)

    class P:
        def __init__(self, year):
            self.year = year

    cases = [
        R(comment="Accepted at NeurIPS 2025", journal_ref=None, published=P(2025)),
        R(comment=None, journal_ref="ICLR 2026", published=P(2026)),
        R(comment=None, journal_ref=None, published=P(2025),
          openreview_venueid="ICLR.cc/2025/Conference"),
        R(comment=None, journal_ref=None, published=P(2025),
          anthology_id="2025.acl-long.42"),
        R(comment=None, journal_ref=None, published=P(2025),
          anthology_id="2025.findings-emnlp.7"),
        R(comment=None, journal_ref=None, published=P(2024)),
    ]
    for r in cases:
        print(classify_route(r))
