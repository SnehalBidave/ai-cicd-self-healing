def analyze_logs(log_text: str):
    """
    Simple rule-based analyzer (we will upgrade to AI later)
    """

    log_text = log_text.lower()

    # Dependency issue
    if "modulenotfounderror" in log_text:
        return {
            "category": "Dependency Issue",
            "root_cause": "Missing Python module",
            "fix": "Add missing package to requirements.txt",
            "confidence": 0.85
        }

    # Test failure
    if "assert" in log_text:
        return {
            "category": "Test Failure",
            "root_cause": "Assertion failed in test",
            "fix": "Fix test case or application logic",
            "confidence": 0.80
        }

    # Default case
    return {
        "category": "Unknown",
        "root_cause": "Could not determine",
        "fix": "Check logs manually",
        "confidence": 0.50
    }
