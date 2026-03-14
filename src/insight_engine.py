def generate_insight(market_summary: str, competitor_insights: list) -> dict:
    """
    Generate final strategic insights.
    """
    return {
        "market_trend": market_summary,
        "competition": competitor_insights,
        "recommendation": "Focus on product differentiation and pricing advantage."
    }
