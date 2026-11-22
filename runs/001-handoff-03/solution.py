def pending_ids(planned: list[str], done: list[str]) -> list[str]:
    """Return unique unfinished IDs in their first planned order."""
    excluded = set(done)
    pending = []
    for item in planned:
        if item not in excluded:
            pending.append(item)
            excluded.add(item)
    return pending
