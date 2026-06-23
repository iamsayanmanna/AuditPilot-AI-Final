def generate_report(
    case,
    audit_result,
    compliance_result,
    risk_score,
    risk_level,
    recommendation
):

    print("\n")
    print("=" * 40)
    print("AUDITPILOT EXECUTIVE REPORT")
    print("=" * 40)

    print(f"\nCase ID: {case['case_id']}")
    print(f"Client ID: {case['client_id']}")
    print(f"Merchant ID: {case['merchant_id']}")

    print(f"\nTransaction Amount: ${abs(case['amount'])}")

    print("\nAUDIT FINDING")
    print(f"{audit_result['finding']}")

    print("\nCOMPLIANCE STATUS")
    print(compliance_result["status"])

    print("\nRISK SCORE")
    print(f"{risk_score}/100")

    print("\nRISK LEVEL")
    print(risk_level)

    print("\nBUSINESS IMPACT")
    print(
        "Potential financial anomaly detected "
        "requiring management attention."
    )

    print("\nRECOMMENDED ACTION")
    print(recommendation)

    print("\n" + "=" * 40)