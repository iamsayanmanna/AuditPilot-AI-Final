def calculate_risk(case):

    risk_score = 0

    amount = abs(case["amount"])

    # Amount Risk
    if amount > 500:
        risk_score += 40
    elif amount > 100:
        risk_score += 25
    else:
        risk_score += 10

    # Negative Transaction Risk
    if case["amount"] < 0:
        risk_score += 30

    # Error Risk
    if case["errors"] != "NONE":
        risk_score += 20

    # Chip Usage Risk
    if case["use_chip"] == "No":
        risk_score += 10

    if risk_score > 100:
        risk_score = 100

    return risk_score