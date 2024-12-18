import ast
from typing import Dict, Any

class ASTTransformer(ast.NodeTransformer):
    """Strips docstrings and line numbers for structural equivalence."""
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, (ast.Str, ast.Constant)):
            node.body = node.body[1:] or [ast.Pass()]
        return node

class ASTEquivalenceChecker:
    """Compares two Python code snippets by inspecting parsed abstract syntax trees."""
    
    @classmethod
    def are_equivalent(cls, code1: str, code2: str, ignore_docstrings: bool = True) -> Dict[str, Any]:
        try:
            tree1 = ast.parse(code1.strip())
            tree2 = ast.parse(code2.strip())
        except SyntaxError as e:
            return {"equivalent": False, "error": f"Syntax error: {str(e)}"}
            
        if ignore_docstrings:
            transformer = ASTTransformer()
            tree1 = transformer.visit(tree1)
            tree2 = transformer.visit(tree2)
            
        dump1 = ast.dump(tree1, include_attributes=False)
        dump2 = ast.dump(tree2, include_attributes=False)
        return {"equivalent": (dump1 == dump2), "syntax_valid": True}
