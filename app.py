import json
from src.compressor import compress_text
from src.analyzer import analyze_competitors
from src.insight_engine import generate_insight


def load_report():
    with open("data/raw_reports/sample_report.txt", "r") as f:
        return f.read()

def load_competitors():
    with open("data/competitors/competitors.json", "r") as f:
        return json.load(f)

def main():
    print("=== Market Intelligence Platform ===")

    market_text = load_report()
    compressed_market = compress_text(market_text)

    competitors = load_competitors()
    competitor_results = analyze_competitors(competitors)

    final_insight = generate_insight(compressed_market, competitor_results)

    print("\n--- Strategic Insight ---")
    for key, value in final_insight.items():
        print(f"\n{key.upper()}:")
        print(value)

if __name__ == "__main__":
    main()
