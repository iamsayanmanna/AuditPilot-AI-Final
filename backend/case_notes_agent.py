import sqlite3

def add_case_note(case_id, note):

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS case_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT,
            note TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO case_notes
        (case_id, note)
        VALUES (?, ?)
    """, (case_id, note))

    conn.commit()
    conn.close()

    return "NOTE SAVED"