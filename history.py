import json
import os
from datetime import datetime

HISTORY_FILE = "outputs/scan_history.json"


def save_scan(prompt, risk_level, score):
    """
    Save every scan to a JSON history file.
    """

    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "prompt": prompt,
        "risk_level": risk_level,
        "anomaly_score": round(score, 4)
    }

    history = []

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)
        except:
            history = []

    history.append(record)

    os.makedirs("outputs", exist_ok=True)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)