from audit_agent import audit_case
from risk_agent import calculate_risk
from compliance_agent import check_compliance
from fraud_agent import detect_fraud_pattern
from alert_agent import generate_alert
from mcp_server import MCPServer
from agent_registry import AGENTS

mcp = MCPServer()


registered_agents = list(
    AGENTS.keys()
)

def run_investigation(case):
    risk_data = mcp.request_tool(
        "RISK_TOOL",
        case
    )

    compliance_data = mcp.request_tool(
        "COMPLIANCE_TOOL",
        case
    )

    audit_data = mcp.request_tool(
        "AUDIT_TOOL",
        case
    )

    audit_result = audit_case(case)
    risk_score = calculate_risk(case)
    compliance_result = check_compliance(case)

    fraud_result = detect_fraud_pattern(
        case["amount"],
        "NORMAL",
        "LOW"
    )

    alert_result = generate_alert(fraud_result)

    return {
        "audit_result": audit_result,
        "risk_score": risk_score,
        "compliance_result": compliance_result,
        "fraud_result": fraud_result,
        "alert_result": alert_result,
        "mcp_tools_used": [
            "AUDIT_TOOL",
            "RISK_TOOL",
            "COMPLIANCE_TOOL"
        ]

        ,"registered_agents": registered_agents,
    }
