def generate_alert(fraud_result):

    if fraud_result["fraud_detected"]:

        return {
            "alert": True,
            "severity": "CRITICAL",
            "message": (
                "Potential fraud detected. "
                "Immediate management review required."
            )
        }

    return {
        "alert": False,
        "severity": "NORMAL",
        "message": (
            "No critical issues detected."
        )
    }