import unittest
from llm_eval.scorers.jaccard import JaccardScorer


class TestJaccardScorer(unittest.TestCase):
    def test_identical_tokens(self):
        res = JaccardScorer.score("apple banana orange", "apple banana orange")
        self.assertEqual(res["score"], 1.0)
        self.assertTrue(res["passed"])

    def test_partial_overlap(self):
        res = JaccardScorer.score("apple banana", "banana orange")
        # 1 common / 3 total unique = 0.3333
        self.assertEqual(res["score"], 0.3333)
        self.assertFalse(res["passed"])

    def test_disjoint_tokens(self):
        res = JaccardScorer.score("apple banana", "cat dog")
        self.assertEqual(res["score"], 0.0)
        self.assertFalse(res["passed"])


if __name__ == '__main__':
    unittest.main()
