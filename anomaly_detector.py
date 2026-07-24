import json
import os
from hooks import activations

from hooks import activations

BASELINE_FILE = "outputs/baseline.json"


def load_baseline():
    """
    Load baseline activation statistics.
    """

    if not os.path.exists(BASELINE_FILE):
        raise FileNotFoundError(
            "Baseline file not found. Run sandbox.py first."
        )

    with open(BASELINE_FILE, "r") as file:
        return json.load(file)


def calculate_z_score(current_mean, baseline_mean, baseline_std):
    """
    Calculate z-score safely.
    """

    if baseline_std == 0:
        baseline_std = 1e-6

    return abs(current_mean - baseline_mean) / baseline_std


def analyze_activations():
    """
    Compare current activations with baseline.
    Returns a dictionary containing anomaly scores.
    """

    baseline = load_baseline()

    layer_results = {}
    total_score = 0.0
    count = 0

    for layer_name, tensor in activations.items():

        if layer_name not in baseline:
            continue

        current_mean = tensor.mean().item()
        current_std = tensor.std().item()

        baseline_mean = baseline[layer_name]["mean"]
        baseline_std = baseline[layer_name]["std"]

        z_score = calculate_z_score(
            current_mean,
            baseline_mean,
            baseline_std
        )

        layer_results[layer_name] = {
            "current_mean": round(current_mean, 6),
            "current_std": round(current_std, 6),
            "baseline_mean": round(baseline_mean, 6),
            "baseline_std": round(baseline_std, 6),
            "z_score": round(z_score, 4)
        }

        total_score += z_score
        count += 1

    overall_score = total_score / count if count else 0.0

    return {
        "overall_score": round(overall_score, 4),
        "layer_count": count,
        "layers": layer_results
    }


def classify_anomaly(score):
    """
    Convert anomaly score into a label.
    """

    if score < 1.0:
        return "NORMAL"
    elif score < 2.5:
        return "SUSPICIOUS"
    else:
        return "ANOMALOUS"


if __name__ == "__main__":
    try:
        result = analyze_activations()

        print("Overall Score :", result["overall_score"])
        print("Classification :", classify_anomaly(result["overall_score"]))

        print("\nLayer Scores:")
        for layer, data in result["layers"].items():
            print(f"{layer}: z={data['z_score']}")

    except Exception as e:
        print("Error:", e)