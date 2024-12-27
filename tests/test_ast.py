import unittest
from llm_eval.code.ast_checker import ASTEquivalenceChecker

class TestASTEquivalenceChecker(unittest.TestCase):
    def test_identical_functions(self):
        c1 = "def add(a, b):\n    return a + b"
        c2 = "def add(a, b):\n    return a + b"
        res = ASTEquivalenceChecker.are_equivalent(c1, c2)
        self.assertTrue(res["equivalent"])

    def test_docstring_removal(self):
        c1 = 'def f(x):\n    """docstring"""\n    return x * 2'
        c2 = 'def f(x):\n    return x * 2'
        res = ASTEquivalenceChecker.are_equivalent(c1, c2, ignore_docstrings=True)
        self.assertTrue(res["equivalent"])

if __name__ == '__main__':
    unittest.main()
