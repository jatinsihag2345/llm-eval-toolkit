# LLM Evaluation Toolkit (`llm-eval-toolkit`)

Modular Python SDK for deterministic grading, AST semantic diffing, and fuzzy scoring of LLM outputs.

## Installation

```bash
pip install llm-eval-toolkit
```

## Quickstart

```python
from llm_eval.scorers.exact import ExactMatchScorer
from llm_eval.scorers.numeric import NumericToleranceScorer

# Exact match with normalization
result = ExactMatchScorer.score("Paris", "paris", case_sensitive=False)
assert result["passed"] is True

# Numeric grading with epsilon tolerance
res = NumericToleranceScorer.score("1.5e-3", 0.0015)
assert res["passed"] is True
```
