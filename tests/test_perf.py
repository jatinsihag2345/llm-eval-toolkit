import unittest
import time
from llm_eval.code.ast_checker import ASTEquivalenceChecker

class TestPerformance(unittest.TestCase):
    def test_ast_speed(self):
        c = "def foo():\n    return 42\n" * 100
        start = time.time()
        ASTEquivalenceChecker.are_equivalent(c, c)
        duration = time.time() - start
        self.assertLess(duration, 0.5)

if __name__ == '__main__':
    unittest.main()
