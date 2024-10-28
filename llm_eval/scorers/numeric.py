import re
from typing import Dict, Any, Union

class NumericToleranceScorer:
    """Validates floating point, integer, and scientific notation answers within epsilon."""
    
    @staticmethod
    def parse_float(val: Union[str, float, int]) -> Union[float, None]:
        if isinstance(val, (int, float)):
            return float(val)
        val_clean = re.sub(r'[^0-9eE.-]', '', str(val))
        try:
            return float(val_clean)
        except ValueError:
            return None

    @classmethod
    def score(cls, prediction: Any, ground_truth: Any, relative_tolerance: float = 1e-4, absolute_tolerance: float = 1e-6) -> Dict[str, Any]:
        p = cls.parse_float(prediction)
        t = cls.parse_float(ground_truth)
        
        if p is None or t is None:
            return {"passed": False, "score": 0.0, "error": "Invalid numeric representation"}
            
        diff = abs(p - t)
        passed = (diff <= absolute_tolerance) or (diff <= relative_tolerance * abs(t))
        return {"passed": passed, "score": 1.0 if passed else 0.0, "parsed_prediction": p, "parsed_truth": t, "diff": diff}
