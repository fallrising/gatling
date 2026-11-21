"""unittest cases for the four input/output pairs in plans/001-handoff.md."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import pending_ids  # noqa: E402


class PendingIdsTest(unittest.TestCase):
    def test_first_seen_order_dedup_and_extra_done(self):
        self.assertEqual(pending_ids(["C", "A", "C", "B"], ["A", "Z"]), ["C", "B"])

    def test_empty_planned(self):
        self.assertEqual(pending_ids([], ["Z"]), [])

    def test_exact_case_sensitive_match(self):
        self.assertEqual(pending_ids(["K", "k"], ["K", "K"]), ["k"])

    def test_all_done(self):
        self.assertEqual(pending_ids(["X"], ["X"]), [])


if __name__ == "__main__":
    unittest.main()
