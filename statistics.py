import json
import os

HISTORY_FILE = "outputs/scan_history.json"


def get_statistics():

    stats = {
        "total": 0,
        "LOW": 0,
        "MEDIUM": 0,
        "HIGH": 0
    }

    if not os.path.exists(HISTORY_FILE):
        return stats

    try:
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

    except Exception:
        return stats

    stats["total"] = len(history)

    for scan in history:

        level = scan.get("risk_level", "").upper()

        if level in stats:
            stats[level] += 1

    return stats