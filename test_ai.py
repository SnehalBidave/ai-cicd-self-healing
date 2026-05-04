from analyzer.ai_analyzer import analyze_logs

# Simulated log
log_data = "AssertionError: assert 2 == 3"

result = analyze_logs(log_data)

print("AI RESULT:")
print(result)
