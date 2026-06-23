case = {
    "case_id": "AP-2026-001",
    "client_id": 1556,
    "merchant_id": 59935,
    "amount": -77.00
}

risk_score = 90
audit_risk = "HIGH"

print("\nEXECUTIVE AGENT")
print("-------------------")

print(f"Case ID: {case['case_id']}")
print(f"Client ID: {case['client_id']}")
print(f"Merchant ID: {case['merchant_id']}")
print(f"Amount: ${case['amount']}")

print(f"\nAudit Risk: {audit_risk}")
print(f"Risk Score: {risk_score}/100")

if risk_score >= 80:
    recommendation = "FREEZE PAYMENT AND ESCALATE TO FINANCE TEAM"
elif risk_score >= 50:
    recommendation = "MANUAL REVIEW REQUIRED"
else:
    recommendation = "APPROVE TRANSACTION"

print("\nEXECUTIVE RECOMMENDATION")
print(recommendation)