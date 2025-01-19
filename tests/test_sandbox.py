import unittest
from llm_eval.code.sandbox import SandboxExecutor

class TestSandboxExecutor(unittest.TestCase):
    def test_successful_run(self):
        runner = SandboxExecutor(timeout_seconds=2.0)
        res = runner.execute("print('Hello from sandbox!')")
        self.assertTrue(res["success"])
        self.assertEqual(res["stdout"].strip(), "Hello from sandbox!")

    def test_timeout_handling(self):
        runner = SandboxExecutor(timeout_seconds=0.5)
        res = runner.execute("import time; time.sleep(2)")
        self.assertTrue(res["timed_out"])
        self.assertFalse(res["success"])

if __name__ == '__main__':
    unittest.main()
