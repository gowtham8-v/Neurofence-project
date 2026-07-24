SUSPICIOUS_KEYWORDS = [

    "ignore previous instructions",
    "ignore all instructions",
    "forget previous instructions",
    "bypass",
    "override",
    "developer mode",
    "system prompt",
    "reveal prompt",
    "jailbreak",
    "disable safety",
    "act as",
    "pretend to be",
    "ignore safety",
    "dan",
    "root access",
    "admin access"

]


def detect_prompt_injection(prompt):

    text = prompt.lower()

    matches = []

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in text:
            matches.append(keyword)

    return {
        "detected": len(matches) > 0,
        "count": len(matches),
        "matches": matches
    }