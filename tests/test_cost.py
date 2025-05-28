import unittest
from llm_eval.telemetry.cost import TokenCostEstimator

class TestTokenCostEstimator(unittest.TestCase):
    def test_gpt4o_cost(self):
        res = TokenCostEstimator.calculate("gpt-4o", 1_000_000, 1_000_000)
        self.assertEqual(res["estimated_cost_usd"], 12.5)

    def test_deepseek_r1_cost(self):
        res = TokenCostEstimator.calculate("deepseek-r1", 1_000_000, 1_000_000)
        self.assertEqual(res["estimated_cost_usd"], 2.74)

if __name__ == '__main__':
    unittest.main()
