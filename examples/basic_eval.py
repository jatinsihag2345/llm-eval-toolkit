from llm_eval.scorers.exact import ExactMatchScorer

samples = [("Berlin", "berlin"), ("42", "42"), ("Yes", "No")]
for pred, truth in samples:
    res = ExactMatchScorer.score(pred, truth)
    print(f"Pred: {pred:<10} | Truth: {truth:<10} | Match: {res['passed']}")
