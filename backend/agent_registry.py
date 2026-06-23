from audit_agent import audit_case
from risk_agent import calculate_risk
from compliance_agent import check_compliance
from fraud_agent import detect_fraud_pattern
from recommendation_agent import generate_recommendation

AGENTS = {
    "AUDIT_AGENT": audit_case,
    "RISK_AGENT": calculate_risk,
    "COMPLIANCE_AGENT": check_compliance,
    "FRAUD_AGENT": detect_fraud_pattern,
    "RECOMMENDATION_AGENT": generate_recommendation
}