import argparse
import json
from llm_eval.scorers.exact import ExactMatchScorer
from llm_eval.scorers.numeric import NumericToleranceScorer

def main():
    parser = argparse.ArgumentParser(description="LLM Evaluation CLI")
    parser.add_argument("--file", required=True, help="Path to JSONL records file")
    parser.add_argument("--metric", choices=["exact", "numeric"], default="exact")
    args = parser.parse_args()

    total, passed = 0, 0
    with open(args.file, "r") as f:
        for line in f:
            if not line.strip(): continue
            item = json.loads(line)
            p = item.get("prediction", "")
            t = item.get("ground_truth", "")
            res = ExactMatchScorer.score(p, t) if args.metric == "exact" else NumericToleranceScorer.score(p, t)
            total += 1
            if res.get("passed"): passed += 1

    accuracy = round((passed / total * 100), 2) if total > 0 else 0.0
    print(f"Evaluated {total} samples | Passed: {passed} | Accuracy: {accuracy}%")

if __name__ == "__main__":
    main()
