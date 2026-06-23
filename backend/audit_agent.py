def audit_case(case):

    if case["amount"] < 0:
        finding = "Negative transaction detected"
        status = "HIGH"
    else:
        finding = "No anomaly detected"
        status = "LOW"

    return {
        "finding": finding,
        "audit_risk": status
    }