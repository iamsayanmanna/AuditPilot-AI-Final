def get_risk_data(case):

    return {
        "amount": case["amount"],
        "errors": case["errors"],
        "use_chip": case["use_chip"]
    }


def get_compliance_data(case):

    return {
        "amount": case["amount"]
    }


def get_audit_data(case):

    return {
        "amount": case["amount"]
    }