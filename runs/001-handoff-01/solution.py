def pending_ids(planned: list[str], done: list[str]) -> list[str]:
    """Return uncompleted IDs in first-planned order, without duplicates."""
    seen = set(done)
    pending = []
    for item in planned:
        if item not in seen:
            seen.add(item)
            pending.append(item)
    return pending
