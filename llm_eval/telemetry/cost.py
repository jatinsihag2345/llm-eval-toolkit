from typing import Dict, Any

MODEL_PRICING = {
    "gpt-4o": {"prompt": 2.50, "completion": 10.00},
    "claude-3-5-sonnet": {"prompt": 3.00, "completion": 15.00},
    "deepseek-r1": {"prompt": 0.55, "completion": 2.19},
    "llama-3-70b": {"prompt": 0.70, "completion": 0.80}
}

class TokenCostEstimator:
    """Calculates USD financial costs for prompt and completion token usages."""
    
    @staticmethod
    def calculate(model_id: str, prompt_tokens: int, completion_tokens: int) -> Dict[str, Any]:
        pricing = MODEL_PRICING.get(model_id.lower(), {"prompt": 2.0, "completion": 8.0})
        p_cost = (prompt_tokens / 1_000_000.0) * pricing["prompt"]
        c_cost = (completion_tokens / 1_000_000.0) * pricing["completion"]
        total = round(p_cost + c_cost, 6)
        return {
            "model_id": model_id,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "estimated_cost_usd": total
        }
