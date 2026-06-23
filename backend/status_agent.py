def get_case_status(risk_score):

    if risk_score >= 80:
        return "UNDER INVESTIGATION"

    elif risk_score >= 60:
        return "PENDING REVIEW"

    elif risk_score >= 40:
        return "ACCOUNTING REVIEW"

    return "APPROVED"