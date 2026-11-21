import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from check_runs import check_record, main

SHA_A = "a" * 40
SHA_B = "b" * 40

VALID = {
    "run_id": "001-handoff-09",
    "case_id": "001-handoff",
    "plan": "plans/001-handoff.md",
    "source_sha": SHA_A,
    "branch": "lab/001-handoff-09",
    "owner": "tester",
    "status": "in_review",
    "updated_at": "2026-11-21T08:00:00+00:00",
    "conditions": {},
    "evidence": [
        {
            "paths": ["runs/001-handoff-09/solution.py"],
            "command": "python3 -m unittest",
            "exit_code": 0,
            "summary": "ok",
        }
    ],
    "outcome": {},
    "human_decision": None,
    "next_prompt": "runs/001-handoff-09/next.md",
}

ACCEPTANCE = {
    "pull_requests": [
        {"url": "https://github.com/example/repo/pull/1", "head": SHA_A, "merge_commit": SHA_B}
    ]
}


class CheckRecordTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for relative in ("plans/001-handoff.md", "runs/001-handoff-09/solution.py", "runs/001-handoff-09/next.md"):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("x\n", encoding="utf-8")
        self.record = self.root / "runs/001-handoff-09/run.json"

    def tearDown(self):
        self._tmp.cleanup()

    def check(self, data):
        self.record.write_text(json.dumps(data), encoding="utf-8")
        return check_record(self.root, self.record)

    def variant(self, **changes):
        data = copy.deepcopy(VALID)
        data.update(changes)
        return data

    def test_valid_record_passes(self):
        self.assertEqual(self.check(VALID), [])

    def test_null_next_prompt_is_allowed(self):
        self.assertEqual(self.check(self.variant(next_prompt=None)), [])

    def test_invalid_json_is_reported(self):
        self.record.write_text("{", encoding="utf-8")
        self.assertEqual(len(check_record(self.root, self.record)), 1)

    def test_missing_key_is_reported(self):
        data = self.variant()
        del data["owner"]
        self.assertEqual(self.check(data), ["missing key: owner"])

    def test_run_id_must_match_directory(self):
        self.assertEqual(len(self.check(self.variant(run_id="001-handoff-08"))), 1)

    def test_short_sha_is_rejected(self):
        self.assertEqual(len(self.check(self.variant(source_sha="aaaaaaa"))), 1)

    def test_unknown_status_is_rejected(self):
        self.assertEqual(len(self.check(self.variant(status="merged"))), 1)

    def test_timestamp_needs_time_zone(self):
        self.assertEqual(len(self.check(self.variant(updated_at="2026-11-21T08:00:00"))), 1)

    def test_missing_evidence_file_is_reported(self):
        data = self.variant()
        data["evidence"][0]["paths"].append("runs/001-handoff-09/absent.txt")
        self.assertEqual(len(self.check(data)), 1)

    def test_path_outside_repository_is_rejected(self):
        self.assertEqual(len(self.check(self.variant(plan="../plans/001-handoff.md"))), 1)

    def test_exit_code_must_be_integer(self):
        data = self.variant()
        data["evidence"][0]["exit_code"] = "0"
        self.assertEqual(len(self.check(data)), 1)

    def test_accepted_requires_acceptance_record(self):
        self.assertEqual(len(self.check(self.variant(status="accepted"))), 1)

    def test_accepted_with_acceptance_record_passes(self):
        self.assertEqual(self.check(self.variant(status="accepted", outcome={"acceptance": ACCEPTANCE})), [])

    def test_accepted_merge_commit_must_be_full_sha(self):
        acceptance = copy.deepcopy(ACCEPTANCE)
        acceptance["pull_requests"][0]["merge_commit"] = "872a7fd"
        self.assertEqual(len(self.check(self.variant(status="accepted", outcome={"acceptance": acceptance}))), 1)


class RepositoryRecordsTests(unittest.TestCase):
    def test_committed_records_pass(self):
        root = Path(__file__).resolve().parent.parent
        with redirect_stdout(io.StringIO()) as output:
            code = main(root)
        self.assertEqual(code, 0, output.getvalue())


if __name__ == "__main__":
    unittest.main()
