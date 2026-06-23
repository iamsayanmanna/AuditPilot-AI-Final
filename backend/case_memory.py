import sqlite3

def save_case(
    case,
    risk_score,
    recommendation
):

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO investigations
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