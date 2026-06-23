from case_generator import generate_case
from audit_agent import audit_case
from risk_agent import calculate_risk
from compliance_agent import check_compliance
from report_generator import generate_report
from database import init_db
from case_memory import save_case
from agent_registry import AGENTS
from mcp_server import MCPServer


init_db()


mcp = MCPServer()

registered_agents = list(
    AGENTS.keys()
)

print("\nAUDITPILOT AI")
print("================================")


print("\nAGENTS CLI MODE")
print("================================")

print("\nREGISTERED AGENTS")
print("--------------------------------")

for agent in registered_agents:
    print(agent)

# Create Case
case = generate_case()

print("\nCASE CREATED")
print("--------------------------------")

for key, value in case.items():
    print(f"{key}: {value}")

print("\nMCP TOOL ROUTING")
print("--------------------------------")

print(
    mcp.request_tool(
        "AUDIT_TOOL",
        case
    )
)

print(
    mcp.request_tool(
        "RISK_TOOL",
        case
    )
)

print(
    mcp.request_tool(
        "COMPLIANCE_TOOL",
        case
    )
)


print("\nAUDIT_AGENT EXECUTED")

# Audit Agent
audit_result = audit_case(case)
compliance_result = check_compliance(case)

print("\nAUDIT AGENT")
print("--------------------------------")
print(f"Finding: {audit_result['finding']}")
print(f"Audit Risk: {audit_result['audit_risk']}")


print("\nRISK_AGENT EXECUTED")

# Risk Agent
risk_score = calculate_risk(case)

print("\nRISK AGENT")
print("--------------------------------")
print(f"Risk Score: {risk_score}/100")

if risk_score >= 80:
    risk_level = "CRITICAL"
elif risk_score >= 60:
    risk_level = "HIGH"
elif risk_score >= 40:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

print(f"Risk Level: {risk_level}")

print("\nCOMPLIANCE_AGENT EXECUTED")

print("\nCOMPLIANCE AGENT")
print("--------------------------------")
print(f"Status: {compliance_result['status']}")
print(f"Message: {compliance_result['message']}")
print(f"Policy Limit: ${compliance_result['policy_limit']}")


# Executive Decision
print("\nEXECUTIVE DECISION")
print("--------------------------------")

if compliance_result["status"] == "VIOLATION":
    recommendation = "REQUIRE CFO APPROVAL"

elif risk_score >= 80:
    recommendation = "FREEZE PAYMENT AND ESCALATE TO FINANCE TEAM"

elif risk_score >= 60:
    recommendation = "MANUAL REVIEW REQUIRED"

elif risk_score >= 40:
    recommendation = "REVIEW WITH ACCOUNTING TEAM"

else:
    recommendation = "APPROVE TRANSACTION"

print(f"Recommendation: {recommendation}")

generate_report(
    case,
    audit_result,
    compliance_result,
    risk_score,
    risk_level,
    recommendation
)


save_case(
    case,
    risk_score,
    recommendation
)

print("\nCASE SAVED TO MEMORY")

print("\nAGENT WORKFLOW COMPLETE")
print("================================")