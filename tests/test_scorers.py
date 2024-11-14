import unittest
from llm_eval.scorers.exact import ExactMatchScorer
from llm_eval.scorers.numeric import NumericToleranceScorer

class TestExactMatchScorer(unittest.TestCase):
    def test_exact_match(self):
        res = ExactMatchScorer.score("Paris", "Paris")
        self.assertTrue(res["passed"])

class TestNumericToleranceScorer(unittest.TestCase):
    def test_float_tolerance(self):
        res = NumericToleranceScorer.score("3.141592", "3.141590", relative_tolerance=1e-4)
        self.assertTrue(res["passed"])

    def test_scientific_notation(self):
        res = NumericToleranceScorer.score("1.5e-3", 0.0015)
        self.assertTrue(res["passed"])

if __name__ == '__main__':
    unittest.main()
