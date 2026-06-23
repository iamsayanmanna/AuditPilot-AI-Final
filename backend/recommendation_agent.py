def generate_recommendation(
    risk_score,
    risk_level
):

    if risk_score >= 80:

        return [
            "Freeze Payment Immediately",
            "Escalate To Finance Manager",
            "Conduct Vendor Audit"
        ]

    elif risk_score >= 60:

        return [
            "Review With Accounting Team",
            "Request Additional Documents",
            "Monitor Vendor Activity"
        ]

    elif risk_score >= 40:

        return [
            "Perform Manual Review",
            "Validate Invoice Details"
        ]

    return [
        "Approve Transaction"
    ]