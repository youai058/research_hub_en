"""Path batching helper for A-3 paper-summarizer sequential dispatch.

The only public function is `chunk_paths`. It is kept trivial + testable so
that the markdown orchestration in `.claude/commands/research-papers.md` can
reference a concrete implementation instead of an inline pseudo-comprehension.
"""

from __future__ import annotations


def chunk_paths(paths: list[str], batch_size: int = 5) -> list[list[str]]:
    """Split `paths` into consecutive batches of at most `batch_size`.

    Args:
        paths: list of absolute paths (strings). Order is preserved.
        batch_size: positive int. Defaults to 5 per design spec §3.4.

    Returns:
        List of batches. An empty input yields an empty list.

    Raises:
        ValueError: if batch_size <= 0.
    """
    if batch_size <= 0:
        raise ValueError(f"batch_size must be positive, got {batch_size}")
    return [paths[i : i + batch_size] for i in range(0, len(paths), batch_size)]
