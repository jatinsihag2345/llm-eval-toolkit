import unittest
from llm_eval.scorers.exact import ExactMatchScorer

class TestExactMatchEdgeCases(unittest.TestCase):
    def test_unicode_whitespace(self):
        res = ExactMatchScorer.score("answer\n\t", "answer")
        self.assertTrue(res["passed"])

if __name__ == '__main__':
    unittest.main()
