import sqlite3

def init_db():

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS investigations (
        case_id TEXT,
        client_id INTEGER,
        merchant_id INTEGER,
        amount REAL,
        risk_score INTEGER,
        recommendation TEXT
    )
    """)

    conn.commit()
    conn.close()