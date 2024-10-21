import unittest
from llm_eval.scorers.exact import ExactMatchScorer

class TestExactMatchScorer(unittest.TestCase):
    def test_exact_match(self):
        res = ExactMatchScorer.score("Paris", "Paris")
        self.assertTrue(res["passed"])
        self.assertEqual(res["score"], 1.0)

    def test_case_insensitive(self):
        res = ExactMatchScorer.score("paris", "Paris", case_sensitive=False)
        self.assertTrue(res["passed"])

    def test_mismatch(self):
        res = ExactMatchScorer.score("London", "Paris")
        self.assertFalse(res["passed"])

if __name__ == '__main__':
    unittest.main()
