from model_loader import load_model
from hooks import activations
from hook_manager import attach_hooks, remove_hooks
from anomaly_detector import analyze_activations, classify_anomaly

def scan(prompt):

    tokenizer, model = load_model()
    activations.clear()

    handles = attach_hooks(model)

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=100,
        do_sample=True,
        temperature=0.7
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )
    remove_hooks(handles)
        # -------------------------------
    # Analyze activations
    # -------------------------------
    analysis = analyze_activations()

    # -------------------------------
    # Calculate overall risk
    # -------------------------------
    overall_score = analysis["overall_score"]
    risk_level = classify_anomaly(overall_score)

    # -------------------------------
    # Return everything
    # -------------------------------
    return {
        "response": response,
        "analysis": analysis,
        "risk_level": risk_level
    }