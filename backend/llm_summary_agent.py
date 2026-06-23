def generate_executive_summary(
    risk_score,
    risk_level,
    finding
):

    return f"""
Executive Summary

Risk Score: {risk_score}
Risk Level: {risk_level}

Finding:
{finding}

Business Impact:
Potential financial risk detected.

Recommended Action:
Review immediately.
"""