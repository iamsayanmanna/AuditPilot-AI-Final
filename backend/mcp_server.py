from mcp_tools import (
    get_risk_data,
    get_compliance_data,
    get_audit_data
)


class MCPServer:

    def request_tool(
        self,
        tool_name,
        case
    ):

        if tool_name == "RISK_TOOL":
            return get_risk_data(case)

        elif tool_name == "COMPLIANCE_TOOL":
            return get_compliance_data(case)

        elif tool_name == "AUDIT_TOOL":
            return get_audit_data(case)

        return {}