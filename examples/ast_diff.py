from llm_eval.code.ast_checker import ASTEquivalenceChecker

c1 = "def square(x): return x ** 2"
c2 = "def square(x):\n    return x ** 2"
res = ASTEquivalenceChecker.are_equivalent(c1, c2)
print(f"Equivalent: {res['equivalent']}")
