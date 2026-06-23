def check_compliance(case):

    amount = abs(case["amount"])

    policy_limit = 500

    if amount > policy_limit:
        status = "VIOLATION"
        message = "Transaction exceeds company spending policy"
    else:
        status = "COMPLIANT"
        message = "Transaction within approved policy"

    return {
        "status": status,
        "message": message,
        "policy_limit": policy_limit
    }