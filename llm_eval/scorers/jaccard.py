from typing import Dict, Any, Set


class JaccardScorer:
    """Calculates Jaccard similarity coefficient between prediction and ground truth token sets."""

    @staticmethod
    def score(prediction: str, ground_truth: str) -> Dict[str, Any]:
        p_tokens = set(prediction.strip().lower().split())
        t_tokens = set(ground_truth.strip().lower().split())

        if not p_tokens and not t_tokens:
            return {"passed": True, "score": 1.0, "intersection": 0, "union": 0}

        intersection = len(p_tokens & t_tokens)
        union = len(p_tokens | t_tokens)
        sim = round(intersection / union, 4) if union > 0 else 0.0

        return {
            "passed": sim > 0.5,
            "score": sim,
            "intersection": intersection,
            "union": union
        }
