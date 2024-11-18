import unittest
from llm_eval.scorers.numeric import NumericToleranceScorer

class TestNumericEdgeCases(unittest.TestCase):
    def test_invalid_string(self):
        res = NumericToleranceScorer.score("not_a_number", 10.0)
        self.assertFalse(res["passed"])

if __name__ == '__main__':
    unittest.main()
