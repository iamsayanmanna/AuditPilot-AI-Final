import token

from flask import Flask, jsonify
from flask_cors import CORS
from case_generator import generate_case
from audit_agent import audit_case
from risk_agent import calculate_risk
from compliance_agent import check_compliance
import sqlite3
from flask import request
import pdfplumber
import re
from invoice_matcher import match_invoice
from coordinator_agent import run_investigation
from status_agent import get_case_status
from approval_agent import get_approval_decision
from llm_summary_agent import generate_executive_summary
from auth_agent import authenticate
from rbac_agent import get_permissions
from case_notes_agent import add_case_note
from audit_log_agent import log_action, get_logs
from recommendation_agent import generate_recommendation
from nl_investigation_agent import investigate_query
from auth_agent import authenticate, validate_token
from rbac_agent import get_permissions, has_permission
from flask import send_file
from pdf_report_agent import generate_pdf_report


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AuditPilot AI API Running"

@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "project": "AuditPilot AI"
    })


@app.route("/test-auth")
def test_auth():

    result = authenticate(
        "admin",
        "admin123"
    )

    return jsonify(result)

@app.route("/login")
def login():

    result = authenticate(
        "admin",
        "admin123"
    )

    return jsonify(result)


@app.route("/permissions/<role>")
def permissions(role):

    permissions = get_permissions(
        role.upper()
    )

    return jsonify({
        "role": role.upper(),
        "permissions": permissions
    })

@app.route("/secure-logs")
def secure_logs():

    token = request.args.get("token")

    if not validate_token(token):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    return jsonify({
        "message": "Access Granted"
    })

@app.route("/secure-permissions")
def secure_permissions():

    role = request.args.get("role")

    if not has_permission(
        role,
        "VIEW_LOGS"
    ):
        return jsonify({
            "error": "Access Denied"
        }), 403

    return jsonify({
        "message": "Permission Granted"
    })

@app.route("/add-note", methods=["POST"])
def add_note():

    data = request.json

    case_id = data["case_id"]
    note = data["note"]

    result = add_case_note(
        case_id,
        note
    )

    return jsonify({
        "status": result
    })

@app.route("/nl-investigation", methods=["POST"])
def nl_investigation():

    data = request.json

    query = data["query"]

    result = investigate_query(query)

    return jsonify({
        "result": result
    })

@app.route("/investigate")
def investigate():

    case = generate_case()

    result = run_investigation(case)

    alert_result = result["alert_result"]

    audit_result = result["audit_result"]

    risk_score = result["risk_score"]

    case_status = get_case_status(risk_score)

    approval_decision = get_approval_decision(risk_score)

    compliance_result = result["compliance_result"]
    

    if risk_score >= 80:
     risk_level = "CRITICAL"
    elif risk_score >= 60:
     risk_level = "HIGH"
    elif risk_score >= 40:
     risk_level = "MEDIUM"
    else:
     risk_level = "LOW"

    executive_summary = generate_executive_summary(
        risk_score,
        risk_level,
        audit_result["finding"]
    )

    ai_recommendations = generate_recommendation(
    risk_score,
    risk_level
)

    recommendation = "REVIEW WITH ACCOUNTING TEAM"

    log_action(
    f"Investigation executed: {case['case_id']}"
)

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO investigations
        (case_id, client_id, merchant_id, amount, risk_score, recommendation)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            case["case_id"],
            case["client_id"],
            case["merchant_id"],
            case["amount"],
            risk_score,
            recommendation
        ))

    conn.commit()
    conn.close()

    return jsonify({
            "case_id": case["case_id"],
            "amount": case["amount"],
            "risk_score": risk_score,
            "risk_level": risk_level,
            "audit_finding": audit_result["finding"],
            "compliance_status": compliance_result["status"],
            "case_status": case_status,
            "approval_decision": approval_decision,
            "executive_summary": executive_summary,
            "ai_recommendations": ai_recommendations,
            "mcp_tools_used": result["mcp_tools_used"],
            "registered_agents":
    result["registered_agents"],
            "alert_message": alert_result["message"],
"alert_severity": alert_result["severity"]
        })

@app.route("/upload-invoice", methods=["POST"])
def upload_invoice():

    file = request.files["invoice"]

    with pdfplumber.open(file) as pdf:

        text = ""

        for page in pdf.pages:
            text += page.extract_text() + "\n"

    invoice_match = re.search(
        r"NO\.\s*(\d+)",
        text
    )

    amount_match = re.search(
        r"TOTAL AMOUNT\s*\$?(\d+)",
        text
    )

    invoice_number = (
        invoice_match.group(1)
        if invoice_match
        else "Unknown"
    )

    amount = (
        float(amount_match.group(1))
        if amount_match
        else 0
    )

    match_result = match_invoice(amount)

    return jsonify({
    "invoice_number": invoice_number,
    "amount": amount,
    "match_status": match_result["status"],
    "risk": match_result["risk"]
})


@app.route("/logs")
def logs():

    token = request.args.get("token")

    if not validate_token(token):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    return jsonify(
        get_logs()
    )


@app.route("/history")
def history():
    token = request.args.get("token")

    if not validate_token(token):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT case_id, amount, risk_score, recommendation
        FROM investigations
        ORDER BY rowid DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:
        history.append({
            "case_id": row[0],
            "amount": row[1],
            "risk_score": row[2],
            "recommendation": row[3]
        })

    return jsonify(history)


@app.route("/export-report")
def export_report():

    report_data = {
        "Project": "AuditPilot AI",
        "Status": "Investigation Complete",
        "Platform": "Enterprise Financial Investigation Platform"
    }

    pdf_file = generate_pdf_report(
        report_data
    )

    print(pdf_file)

    return send_file(
        pdf_file,
        as_attachment=True
    )



@app.route("/stats")
def stats():

    token = request.args.get("token")

    if not validate_token(token):

        return jsonify({
            "error": "Unauthorized"
        }), 401

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM investigations"
    )
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM investigations WHERE risk_score >= 60"
    )
    high_risk = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total_investigations": total,
        "high_risk_cases": high_risk,
        "compliance_alerts": 0,
        "invoices_analyzed": 1
    })


@app.errorhandler(Exception)
def handle_exception(error):

    log_action(
        f"SYSTEM ERROR: {str(error)}"
    )

    return jsonify({
        "status": "error",
        "message": "Internal Server Error",
        "details": str(error)
    }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)