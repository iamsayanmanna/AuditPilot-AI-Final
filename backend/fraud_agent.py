def detect_fraud_pattern(
    amount,
    duplicate_status,
    vendor_risk
):

    flags = []

    if abs(amount) > 500:
        flags.append("LARGE_TRANSACTION")

    if duplicate_status == "DUPLICATE INVOICE":
        flags.append("DUPLICATE_INVOICE")

    if vendor_risk == "HIGH":
        flags.append("HIGH_RISK_VENDOR")

    if len(flags) >= 2:

        return {
            "fraud_detected": True,
            "risk_level": "HIGH",
            "flags": flags
        }

    return {
        "fraud_detected": False,
        "risk_level": "LOW",
        "flags": flags
    }