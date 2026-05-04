def analyze_logs(log_text: str):

    log_text = log_text.lower()

    if "assert" in log_text:
        return {
            "category": "Test Failure",
            "root_cause": "Assertion failed",
            "fix": "Check test case or logic",
            "confidence": 0.8
        }

    if "error" in log_text:
        return {
            "category": "General Error",
            "root_cause": "Error found in logs",
            "fix": "Check logs carefully",
            "confidence": 0.6
        }

    return {
        "category": "Unknown",
        "root_cause": "Not identified",
        "fix": "Manual check required",
        "confidence": 0.5
    }
