def get_approval_decision(risk_score):

    if risk_score >= 80:
        return "REJECTED"

    elif risk_score >= 60:
        return "MANAGER APPROVAL REQUIRED"

    elif risk_score >= 40:
        return "ACCOUNTING APPROVAL REQUIRED"

    return "AUTO APPROVED"