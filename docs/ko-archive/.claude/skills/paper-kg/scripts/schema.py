"""Pydantic schema for paper-kg `.kg.json` files.

Defines node/edge types, pinned ID regex, and file envelope.
Used by index.py, query.py, and kg-curator for validation.
"""

from __future__ import annotations

import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

SCHEMA_VERSION = "1-stable"

ALIAS_BOOTSTRAP_THRESHOLD = 50

NODE_TYPES = (
    "Paper",
    "Author",
    "Venue",
    "Claim",
    "Method",
    "Dataset",
    "Model",
    "Metric",
    "Result",
    "Idea",
    "Critique",
    "Hypothesis",
    "Plan",
    "Experiment",
    "Diagnosis",
    "Lesson",
    "LoopIteration",
    # Answer-loop nodes (2026-04-15): user question → grounded answer → evidence verification
    "Question",
    "Answer",
    "Evidence",
)

NodeType = Literal[
    "Paper",
    "Author",
    "Venue",
    "Claim",
    "Method",
    "Dataset",
    "Model",
    "Metric",
    "Result",
    "Idea",
    "Critique",
    "Hypothesis",
    "Plan",
    "Experiment",
    "Diagnosis",
    "Lesson",
    "LoopIteration",
    "Question",
    "Answer",
    "Evidence",
]

TYPE_TO_PREFIX = {
    "Paper": "paper",
    "Author": "author",
    "Venue": "venue",
    "Claim": "claim",
    "Method": "method",
    "Dataset": "dataset",
    "Model": "model",
    "Metric": "metric",
    "Result": "result",
    "Idea": "idea",
    "Critique": "critique",
    "Hypothesis": "hypothesis",
    "Plan": "plan",
    "Experiment": "experiment",
    "Diagnosis": "diagnosis",
    "Lesson": "lesson",
    "LoopIteration": "loop",
    "Question": "question",
    "Answer": "answer",
    "Evidence": "evidence",
}

EDGE_TYPES = (
    # Paper intrinsic
    "WROTE",
    "PUBLISHED_AT",
    "MAKES",
    "PROPOSES",
    "EVALUATES_ON",
    "USES_MODEL",
    "MEASURES_WITH",
    "REPORTS",
    "EVIDENCED_BY",
    "OF_METRIC",
    # Research loop provenance
    "INSPIRED_BY",
    "CHALLENGES",
    "EXTENDS",
    "EVALUATES",
    "CITES",
    "DERIVED_FROM",
    "CONTAINS",
    "MEASURES",
    "TESTED_BY",
    "IMPLEMENTS",
    "USES_METHOD",
    "ON_DATASET",
    "ON_MODEL",
    "PRODUCES",
    "REPRODUCES",
    "ANALYZES",
    "BLAMES",
    "LEARNED_FROM",
    "PRODUCED",
    # Paper-summarize aliases (co-exist with WROTE/PUBLISHED_AT/MAKES/REPORTS; direction-semantic variants)
    "AUTHORED_BY",
    "PUBLISHED_IN",
    "MAKES_CLAIM",
    "REPORTS_RESULT",
    # Answer-Evidence loop (B-1/B-2/C-1/E-1/F-1 paradigm, 2026-04-15)
    "ADDRESSES",       # Answer --> Question
    "GROUNDED_IN",     # Evidence --> Paper | Claim
    "REVIEWS",         # Critique --> Answer
    "CONTRADICTS",     # Critique --> Claim
    "FLAGS_WEAK",      # Critique --> Evidence
    "VERIFIES",        # Plan --> Answer; Experiment --> Evidence
    "USES_DATASET",    # Plan | Experiment --> Dataset
    "USES_METRIC",     # Plan --> Metric
    "COMPARES_WITH",   # Plan --> Method (baseline)
    "ABOUT",           # Diagnosis --> Experiment
    "CONCERNS",        # Diagnosis --> Answer
    "SUGGESTS_NEXT",   # Diagnosis --> Answer (revision seed)
    # Special curator-handled edge
    "alias_merge",
)

EdgeType = Literal[
    "WROTE",
    "PUBLISHED_AT",
    "MAKES",
    "PROPOSES",
    "EVALUATES_ON",
    "USES_MODEL",
    "MEASURES_WITH",
    "REPORTS",
    "EVIDENCED_BY",
    "OF_METRIC",
    "INSPIRED_BY",
    "CHALLENGES",
    "EXTENDS",
    "EVALUATES",
    "CITES",
    "DERIVED_FROM",
    "CONTAINS",
    "MEASURES",
    "TESTED_BY",
    "IMPLEMENTS",
    "USES_METHOD",
    "ON_DATASET",
    "ON_MODEL",
    "PRODUCES",
    "REPRODUCES",
    "ANALYZES",
    "BLAMES",
    "LEARNED_FROM",
    "PRODUCED",
    "AUTHORED_BY",
    "PUBLISHED_IN",
    "MAKES_CLAIM",
    "REPORTS_RESULT",
    "ADDRESSES",
    "GROUNDED_IN",
    "REVIEWS",
    "CONTRADICTS",
    "FLAGS_WEAK",
    "VERIFIES",
    "USES_DATASET",
    "USES_METRIC",
    "COMPARES_WITH",
    "ABOUT",
    "CONCERNS",
    "SUGGESTS_NEXT",
    "alias_merge",
]

Polarity = Literal["support", "contradict", "mixed"]

# Nodes requiring alias_check (canonical-entity types).
ALIAS_REQUIRED_TYPES = {"Method", "Dataset", "Model", "Metric"}

# Pinned ID regex. `#` is accepted but slash commands must quote it;
# alt form `--` is accepted in place of `#`.
ID_REGEX = re.compile(
    r"^(paper|author|venue|claim|method|dataset|model|metric|result|"
    r"idea|critique|hypothesis|plan|experiment|diagnosis|lesson|loop|"
    r"question|answer|evidence)"
    r":[a-z0-9][a-z0-9\-/]*(#[a-z0-9\-]+|--[a-z0-9\-]+)?$"
)


def normalize_id(raw: str) -> str:
    """Normalize `--local` alt form to `#local`."""
    if "--" in raw and "#" not in raw:
        prefix, _, local = raw.partition("--")
        return f"{prefix}#{local}"
    return raw


def id_prefix(node_id: str) -> str:
    return node_id.split(":", 1)[0]


class AliasCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")
    queried_existing: bool
    matched: str | None = None
    rationale: str


class KGNode(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    type: NodeType
    name: str
    meta: dict[str, Any] = Field(default_factory=dict)
    alias_check: AliasCheck | None = None

    @field_validator("id")
    @classmethod
    def _validate_id(cls, v: str) -> str:
        v = normalize_id(v)
        if not ID_REGEX.match(v):
            raise ValueError(f"node id does not match pinned regex: {v!r}")
        return v

    @model_validator(mode="after")
    def _validate_type_prefix(self) -> "KGNode":
        expected = TYPE_TO_PREFIX[self.type]
        got = id_prefix(self.id)
        if got != expected:
            raise ValueError(
                f"id prefix {got!r} does not match type {self.type!r} "
                f"(expected {expected!r})"
            )
        return self


class KGEdge(BaseModel):
    model_config = ConfigDict(extra="forbid")

    src: str
    type: EdgeType
    dst: str
    meta: dict[str, Any] = Field(default_factory=dict)

    @field_validator("src", "dst")
    @classmethod
    def _validate_endpoint(cls, v: str) -> str:
        v = normalize_id(v)
        if not ID_REGEX.match(v):
            raise ValueError(f"edge endpoint does not match pinned regex: {v!r}")
        return v

    @model_validator(mode="after")
    def _validate_polarity(self) -> "KGEdge":
        if self.type == "EVIDENCED_BY":
            pol = self.meta.get("polarity")
            if pol not in ("support", "contradict", "mixed"):
                raise ValueError(
                    "EVIDENCED_BY edge requires meta.polarity ∈ "
                    "{support, contradict, mixed}"
                )
        return self


class KGFile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    version: int
    source_file: str
    source_sha: str
    author_agent: str
    extracted_at: str
    nodes: list[KGNode] = Field(default_factory=list)
    edges: list[KGEdge] = Field(default_factory=list)

    @field_validator("version")
    @classmethod
    def _validate_version(cls, v: int) -> int:
        if v != 1:
            raise ValueError(f"unsupported .kg.json version: {v}")
        return v


def enforce_alias_check(
    node: KGNode, current_node_count: int
) -> tuple[bool, str | None]:
    """Return (ok, error) for alias_check requirement.

    Bootstrap softening: if current_node_count < ALIAS_BOOTSTRAP_THRESHOLD,
    a node may omit alias_check or set queried_existing=False with rationale.
    """
    if node.type not in ALIAS_REQUIRED_TYPES:
        return True, None
    if node.alias_check is None:
        if current_node_count < ALIAS_BOOTSTRAP_THRESHOLD:
            return True, None
        return (
            False,
            f"node {node.id} type {node.type} requires alias_check "
            f"(kg has {current_node_count} nodes >= {ALIAS_BOOTSTRAP_THRESHOLD})",
        )
    return True, None
