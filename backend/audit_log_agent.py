import sqlite3

def log_action(action):

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO audit_logs(action)
        VALUES (?)
    """, (action,))

    conn.commit()
    conn.close()


def get_logs():

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT action
        FROM audit_logs
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]