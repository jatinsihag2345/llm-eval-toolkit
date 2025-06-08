import unittest
from llm_eval.telemetry.cost import TokenCostEstimator

class TestCostOverride(unittest.TestCase):
    def test_custom_rate(self):
        res = TokenCostEstimator.calculate("custom-llm", 1_000_000, 1_000_000, {"prompt": 1.0, "completion": 2.0})
        self.assertEqual(res["estimated_cost_usd"], 3.0)

if __name__ == '__main__':
    unittest.main()
