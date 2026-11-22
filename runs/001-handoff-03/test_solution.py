import unittest

from solution import pending_ids


class PendingIdsTests(unittest.TestCase):
    def test_first_occurrence_order_and_extra_done(self):
        self.assertEqual(pending_ids(["C", "A", "C", "B"], ["A", "Z"]), ["C", "B"])

    def test_empty_plan(self):
        self.assertEqual(pending_ids([], ["Z"]), [])

    def test_exact_case_and_duplicate_done(self):
        self.assertEqual(pending_ids(["K", "k"], ["K", "K"]), ["k"])

    def test_all_done(self):
        self.assertEqual(pending_ids(["X"], ["X"]), [])


if __name__ == "__main__":
    unittest.main()
