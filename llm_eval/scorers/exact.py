import re
from typing import Dict, Any

class ExactMatchScorer:
    """Strict and normalized exact match scorer."""
    
    @staticmethod
    def score(prediction: str, ground_truth: str, strip_whitespace: bool = True, case_sensitive: bool = False) -> Dict[str, Any]:
        p = prediction.strip() if strip_whitespace else prediction
        t = ground_truth.strip() if strip_whitespace else ground_truth
        
        if not case_sensitive:
            p = p.lower()
            t = t.lower()
            
        is_match = (p == t)
        return {
            "passed": is_match,
            "score": 1.0 if is_match else 0.0,
            "prediction": prediction,
            "ground_truth": ground_truth,
            "normalized_prediction": p,
            "normalized_truth": t
        }
