import json
import os

import torch

from scanner import scan
from hooks import activations


SAFE_PROMPTS = [
    "Hello",
    "What is Artificial Intelligence?",
    "Explain cybersecurity.",
    "What is machine learning?",
    "Describe cloud computing."
]


def generate_baseline():

    baseline = {}

    print("Generating activation baseline...\n")

    for prompt in SAFE_PROMPTS:

        print(f"Scanning: {prompt}")

        scan(prompt)

        for layer_name, tensor in activations.items():

            mean = tensor.mean().item()
            std = tensor.std().item()

            if layer_name not in baseline:
                baseline[layer_name] = {
                    "mean": [],
                    "std": []
                }

            baseline[layer_name]["mean"].append(mean)
            baseline[layer_name]["std"].append(std)

    final_baseline = {}

    for layer_name, values in baseline.items():

        final_baseline[layer_name] = {

            "mean": float(sum(values["mean"]) / len(values["mean"])),

            "std": float(sum(values["std"]) / len(values["std"]))
        }

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/baseline.json", "w") as file:
        json.dump(final_baseline, file, indent=4)

    print("\nBaseline saved successfully.")
    print("Location : outputs/baseline.json")


if __name__ == "__main__":
    generate_baseline()