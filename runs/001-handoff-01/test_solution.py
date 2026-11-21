import unittest

from solution import pending_ids


class PendingIdsTests(unittest.TestCase):
    def test_preserves_first_order_and_ignores_extra_done(self):
        self.assertEqual(pending_ids(["C", "A", "C", "B"], ["A", "Z"]), ["C", "B"])

    def test_empty_planned(self):
        self.assertEqual(pending_ids([], ["Z"]), [])

    def test_exact_case_and_duplicate_done(self):
        self.assertEqual(pending_ids(["K", "k"], ["K", "K"]), ["k"])

    def test_all_done(self):
        self.assertEqual(pending_ids(["X"], ["X"]), [])
