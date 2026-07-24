import json
import os

HISTORY_FILE = "outputs/scan_history.json"


def get_recent_scans(limit=5):

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

    except Exception:
        return []

    history = list(reversed(history))

    return history[:limit]