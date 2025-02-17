from llm_eval.code.sandbox import SandboxExecutor

runner = SandboxExecutor(timeout_seconds=3.0)
code = "import math\nprint(math.factorial(10))"
res = runner.execute(code)
print(f"Output: {res['stdout'].strip()} | Success: {res['success']}")
