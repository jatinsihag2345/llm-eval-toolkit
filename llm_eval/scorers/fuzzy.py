from typing import Dict, Any
from collections import Counter

class FuzzyScorer:
    """Calculates token-level F1, BLEU-1 approximation, and Levenshtein similarity."""
    
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
        m, n = len(s1), len(s2)
        if m == 0 and n == 0:
            return 1.0
        if m == 0 or n == 0:
            return 0.0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): dp[i][0] = i
        for j in range(n + 1): dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if s1[i-1] == s2[j-1] else 1
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
        dist = dp[m][n]
        return round(1.0 - (dist / max(m, n)), 4)
