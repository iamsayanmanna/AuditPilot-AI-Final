def analyze_root_cause(
    amount,
    duplicate_status,
    vendor_risk
):

    causes = []

    if abs(amount) > 500:
        causes.append(
            "Unusually large transaction"
        )

    if duplicate_status == "DUPLICATE INVOICE":
        causes.append(
            "Duplicate invoice detected"
        )

    if vendor_risk == "HIGH":
        causes.append(
            "High risk vendor involved"
        )

    if not causes:
        causes.append(
            "No major anomalies detected"
        )

    return causes