import json
import os
from datetime import datetime


def export_report(prompt, response, analysis, risk):

    os.makedirs("outputs", exist_ok=True)

    filename = datetime.now().strftime(
        "outputs/report_%Y%m%d_%H%M%S.json"
    )

    report = {

        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "prompt": prompt,

        "response": response,

        "risk_level": risk["risk_level"],

        "recommendation": risk["recommendation"],

        "overall_score": analysis["overall_score"],

        "layer_count": analysis["layer_count"],

        "layers": analysis["layers"]

    }

    with open(filename, "w") as file:

        json.dump(report, file, indent=4)

    return filename