"""Fixed task for plans/001-handoff.md: list planned IDs that are still pending."""

from __future__ import annotations


def pending_ids(planned: list[str], done: list[str]) -> list[str]:
    """Return IDs from ``planned`` not in ``done``, in first-seen order, each at most once.

    IDs are compared as exact strings; extra IDs in ``done`` have no effect.
    """
    finished = set(done)
    seen: set[str] = set()
    result: list[str] = []
    for item in planned:
        if item in finished or item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
