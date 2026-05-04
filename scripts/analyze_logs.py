from analyzer.ai_analyzer import analyze_logs

def main():
    try:
        with open("logs/output.log", "r") as f:
            logs = f.read()
    except FileNotFoundError:
        print("No logs found")
        return

    result = analyze_logs(logs)

    print("\n===== AI ANALYSIS RESULT =====\n")

    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
