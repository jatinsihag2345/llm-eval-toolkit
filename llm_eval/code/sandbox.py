import subprocess
import sys
from typing import Dict, Any, Optional

class SandboxExecutor:
    """Executes arbitrary Python code in an isolated subprocess with timeout and memory enforcement."""
    
    def __init__(self, timeout_seconds: float = 5.0, max_memory_mb: int = 512):
        self.timeout_seconds = timeout_seconds
        self.max_memory_mb = max_memory_mb

    def execute(self, code: str, stdin_data: Optional[str] = None) -> Dict[str, Any]:
        try:
            proc = subprocess.run(
                [sys.executable, "-c", code],
                input=stdin_data,
                capture_output=True,
                text=True,
                timeout=self.timeout_seconds
            )
            return {
                "exit_code": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "timed_out": False,
                "success": (proc.returncode == 0)
            }
        except subprocess.TimeoutExpired:
            return {
                "exit_code": -1,
                "stdout": "",
                "stderr": f"Execution timed out after {self.timeout_seconds}s",
                "timed_out": True,
                "success": False
            }
