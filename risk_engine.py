def evaluate_risk(score):

    if score < 1.0:

        return {
            "risk_level": "LOW",
            "recommendation": "Prompt appears safe."
        }

    elif score < 2.5:

        return {
            "risk_level": "MEDIUM",
            "recommendation": "Review the generated response carefully."
        }

    else:

        return {
            "risk_level": "HIGH",
            "recommendation": "Possible abnormal model behaviour detected."
        }