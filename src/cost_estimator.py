def calculate_savings(old_cost: float, new_cost: float) -> dict:
    savings = old_cost - new_cost
    yearly = savings * 12
    roi = (savings / old_cost) * 100 if old_cost else 0

    return {
        "monthly_savings": savings,
        "yearly_savings": yearly,
        "roi_percent": round(roi, 2)
    }
