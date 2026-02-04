def analyze_competitors(competitors: dict) -> list:
    """
    Analyze competitor strengths.
    """
    insights = []

    for name, info in competitors.items():
        strength = info.get("strengths", "No strengths provided")
        insights.append(f"{name} is strong in {strength}")

    return insights
