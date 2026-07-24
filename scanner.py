from model_loader import load_model
from hooks import activations
from hook_manager import attach_hooks, remove_hooks

from anomaly_detector import analyze_activations
from risk_engine import evaluate_risk


def scan(prompt):

    # Load tokenizer and model
    tokenizer, model = load_model()

    # Clear previous activations
    activations.clear()

    # Attach hooks
    handles = attach_hooks(model)

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate response
    outputs = model.generate(
        **inputs,
        max_length=100,
        do_sample=True,
        temperature=0.7
    )

    # Decode response
    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # Remove hooks
    remove_hooks(handles)

    # Analyze activations
    analysis = analyze_activations()

    # Calculate risk
    overall_score = analysis["overall_score"]
    risk = evaluate_risk(overall_score)

    # Return everything
    return {
        "response": response,
        "analysis": analysis,
        "risk": risk
    }