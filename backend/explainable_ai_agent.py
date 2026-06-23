def explain_decision(
    risk_score,
    risk_level,
    root_causes
):

    explanation = f"""
Why was this case flagged?

Risk Score: {risk_score}
Risk Level: {risk_level}

Reasons:
"""

    for cause in root_causes:
        explanation += f"\n- {cause}"

    return explanation