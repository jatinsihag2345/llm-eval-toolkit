from llm_eval.scorers.fuzzy import FuzzyScorer

p = "The quick brown fox jumps over the lazy dog"
t = "A quick brown fox jumped over a lazy dog"

f1 = FuzzyScorer.token_f1(p, t)
sim = FuzzyScorer.levenshtein_similarity(p, t)
print(f"Token F1: {f1['f1']} | Levenshtein Sim: {sim}")
