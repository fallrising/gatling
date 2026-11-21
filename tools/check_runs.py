"""Check every runs/<run-id>/run.json against the format in runs/README.md.

Run from the repository root:  python3 tools/check_runs.py
Exit code 0 means every record passed; 1 means at least one problem was printed.
Only the standard library is used, and nothing is written.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

REQUIRED_KEYS = (
    "run_id", "case_id", "plan", "source_sha", "branch", "owner", "status",
    "updated_at", "conditions", "evidence", "outcome", "human_decision", "next_prompt",
)
STATUSES = {"running", "handoff_ready", "blocked", "in_review", "accepted"}
SHA = re.compile(r"[0-9a-f]{40}")


def _relative_path_problem(root: Path, value: object, field: str) -> str | None:
    if not isinstance(value, str) or not value:
        return f"{field} must be a non-empty repo-relative path"
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        return f"{field} must stay inside the repository: {value}"
    if not (root / path).is_file():
        return f"{field} points to a missing file: {value}"
    return None


def check_record(root: Path, record_path: Path) -> list[str]:
    """Return the problems found in one run.json; an empty list means it passed."""
    try:
        data = json.loads(record_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        return [f"cannot read JSON: {error}"]
    if not isinstance(data, dict):
        return ["top level must be an object"]

    problems = [f"missing key: {key}" for key in REQUIRED_KEYS if key not in data]
    if problems:
        return problems

    if data["run_id"] != record_path.parent.name:
        problems.append(f"run_id {data['run_id']!r} does not match directory {record_path.parent.name!r}")
    if not isinstance(data["source_sha"], str) or not SHA.fullmatch(data["source_sha"]):
        problems.append("source_sha must be a full 40-character lowercase commit SHA")
    if not isinstance(data["branch"], str) or not data["branch"]:
        problems.append("branch must be a non-empty string")
    status = data["status"]
    if status not in STATUSES:
        problems.append(f"status {status!r} is not one of {sorted(STATUSES)}")

    try:
        stamp = datetime.fromisoformat(data["updated_at"])
    except (TypeError, ValueError):
        problems.append("updated_at must be an ISO 8601 timestamp")
    else:
        if stamp.tzinfo is None:
            problems.append("updated_at must include a time zone")

    for field in ("plan", "next_prompt"):
        if field == "next_prompt" and data[field] is None:
            continue
        problem = _relative_path_problem(root, data[field], field)
        if problem:
            problems.append(problem)

    if not isinstance(data["evidence"], list):
        problems.append("evidence must be a list")
    else:
        for index, item in enumerate(data["evidence"]):
            label = f"evidence[{index}]"
            if not isinstance(item, dict):
                problems.append(f"{label} must be an object")
                continue
            if not isinstance(item.get("exit_code"), int) or isinstance(item.get("exit_code"), bool):
                problems.append(f"{label}.exit_code must be an integer")
            paths = item.get("paths")
            if not isinstance(paths, list) or not paths:
                problems.append(f"{label}.paths must be a non-empty list")
                continue
            for path_index, value in enumerate(paths):
                problem = _relative_path_problem(root, value, f"{label}.paths[{path_index}]")
                if problem:
                    problems.append(problem)

    if status == "accepted":
        problems.extend(_acceptance_problems(data["outcome"]))
    return problems


def _acceptance_problems(outcome: object) -> list[str]:
    acceptance = outcome.get("acceptance") if isinstance(outcome, dict) else None
    pulls = acceptance.get("pull_requests") if isinstance(acceptance, dict) else None
    if not isinstance(pulls, list) or not pulls:
        return ["status accepted requires a non-empty outcome.acceptance.pull_requests"]
    problems = []
    for index, pull in enumerate(pulls):
        label = f"outcome.acceptance.pull_requests[{index}]"
        if not isinstance(pull, dict):
            problems.append(f"{label} must be an object")
            continue
        if not isinstance(pull.get("url"), str) or not pull["url"].startswith("https://"):
            problems.append(f"{label}.url must be an https URL")
        for key in ("head", "merge_commit"):
            if not isinstance(pull.get(key), str) or not SHA.fullmatch(pull[key]):
                problems.append(f"{label}.{key} must be a full 40-character lowercase commit SHA")
    return problems


def main(root: Path) -> int:
    records = sorted(root.glob("runs/*/run.json"))
    if not records:
        print("no runs/*/run.json found", file=sys.stderr)
        return 1
    failed = False
    for record in records:
        problems = check_record(root, record)
        relative = record.relative_to(root).as_posix()
        if problems:
            failed = True
            for problem in problems:
                print(f"{relative}: {problem}")
        else:
            print(f"{relative}: ok")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(Path.cwd()))
