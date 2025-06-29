# LLM Evaluation Toolkit (`llm-eval-toolkit`)

[![Test Suite](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Modular Python SDK for deterministic grading, AST semantic diffing, and fuzzy scoring of LLM outputs.

## Architecture

```
llm_eval/
├── scorers/
│   ├── exact.py          # Strict and case-normalized exact match
│   ├── numeric.py        # Epsilon tolerance & LaTeX boxed parser
│   └── fuzzy.py          # Token F1, BLEU-1, and Levenshtein similarity
├── code/
│   ├── ast_checker.py    # Python syntax tree structural equivalence
│   └── sandbox.py        # Subprocess sandbox with memory & timeout limits
└── telemetry/
    └── cost.py           # Multi-model token cost financial auditor
```

## Quickstart

```python
from llm_eval import ExactMatchScorer, NumericToleranceScorer, ASTEquivalenceChecker

# 1. Evaluate Boxed LaTeX Math Answers
res = NumericToleranceScorer.score(r"The solution is \boxed{42.0001}", 42.0)
assert res["passed"] is True

# 2. Check AST Code Equivalence
c1 = "def f(x): return x + 1"
c2 = "def f(x):\n    '''Docstring'''\n    return x + 1"
assert ASTEquivalenceChecker.are_equivalent(c1, c2)["equivalent"] is True
```
