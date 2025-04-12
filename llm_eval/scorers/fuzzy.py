from typing import Dict, Any
from collections import Counter

class FuzzyScorer:
    """Calculates token-level F1, BLEU-1 approximation, and Levenshtein similarity with linear space DP."""
    
    @staticmethod
    def bleu_1(prediction: str, ground_truth: str) -> float:
        p_tokens = prediction.strip().lower().split()
        t_tokens = ground_truth.strip().lower().split()
        if not p_tokens or not t_tokens:
            return 1.0 if p_tokens == t_tokens else 0.0
        p_counts = Counter(p_tokens)
        t_counts = Counter(t_tokens)
        clipped = sum(min(count, t_counts[token]) for token, count in p_counts.items())
        return round(clipped / len(p_tokens), 4)

    @staticmethod
    def token_f1(prediction: str, ground_truth: str) -> Dict[str, float]:
        p_tokens = prediction.strip().lower().split()
        t_tokens = ground_truth.strip().lower().split()
        if not p_tokens or not t_tokens:
            score = 1.0 if p_tokens == t_tokens else 0.0
            return {"precision": score, "recall": score, "f1": score}
        common = set(p_tokens) & set(t_tokens)
        if not common:
            return {"precision": 0.0, "recall": 0.0, "f1": 0.0}
        precision = len(common) / len(p_tokens)
        recall = len(common) / len(t_tokens)
        f1 = (2 * precision * recall) / (precision + recall)
        return {"precision": round(precision, 4), "recall": round(recall, 4), "f1": round(f1, 4)}

    @staticmethod
    def levenshtein_similarity(s1: str, s2: str) -> float:
        if s1 == s2: return 1.0
        m, n = len(s1), len(s2)
        if m == 0 or n == 0: return 0.0
        prev = list(range(n + 1))
        for i, c1 in enumerate(s1, 1):
            curr = [i] * (n + 1)
            for j, c2 in enumerate(s2, 1):
                curr[j] = min(prev[j] + 1, curr[j-1] + 1, prev[j-1] + (0 if c1 == c2 else 1))
            prev = curr
        return round(1.0 - (prev[n] / max(m, n)), 4)
