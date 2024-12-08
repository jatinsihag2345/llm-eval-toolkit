import ast
from typing import Dict, Any

class ASTEquivalenceChecker:
    """Compares two Python code snippets by inspecting parsed abstract syntax trees."""
    
    @classmethod
    def are_equivalent(cls, code1: str, code2: str) -> Dict[str, Any]:
        try:
            tree1 = ast.parse(code1.strip())
            tree2 = ast.parse(code2.strip())
        except SyntaxError as e:
            return {"equivalent": False, "error": f"Syntax error: {str(e)}"}
            
        dump1 = ast.dump(tree1, include_attributes=False)
        dump2 = ast.dump(tree2, include_attributes=False)
        return {"equivalent": (dump1 == dump2), "syntax_valid": True}
