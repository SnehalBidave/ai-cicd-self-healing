def extract_relevant_lines(log_text: str):
    lines = log_text.split("\n")

    important = []
    for line in lines:
        if "error" in line.lower() or "failed" in line.lower() or "assert" in line.lower():
            important.append(line)

    return important[-10:]


def analyze_logs(log_text: str):

    relevant_lines = extract_relevant_lines(log_text)
    combined = " ".join(relevant_lines).lower()

    if "assert" in combined:
        return {
            "category": "Test Failure",
            "root_cause": "Assertion failed in test case",
            "fix": "Check expected vs actual output in test",
            "confidence": 0.85,
            "evidence": relevant_lines
        }

    if "modulenotfounderror" in combined:
        return {
            "category": "Dependency Issue",
            "root_cause": "Missing Python module",
            "fix": "Add required package to requirements.txt",
            "confidence": 0.9,
            "evidence": relevant_lines
        }

    if "syntaxerror" in combined:
        return {
            "category": "Code Issue",
            "root_cause": "Syntax error in code",
            "fix": "Fix syntax in code",
            "confidence": 0.88,
            "evidence": relevant_lines
        }

    if "error" in combined:
        return {
            "category": "General Error",
            "root_cause": "Error found in logs",
            "fix": "Check logs for details",
            "confidence": 0.6,
            "evidence": relevant_lines
        }

    return {
        "category": "Unknown",
        "root_cause": "Not identified",
        "fix": "Manual debugging required",
        "confidence": 0.5,
        "evidence": relevant_lines
    }
