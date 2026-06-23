import sqlite3

def check_duplicate_invoice(invoice_number):

    conn = sqlite3.connect("auditpilot.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            invoice_number TEXT
        )
    """)

    cursor.execute("""
        SELECT COUNT(*)
        FROM invoices
        WHERE invoice_number = ?
    """, (invoice_number,))

    count = cursor.fetchone()[0]

    if count > 0:
        result = "DUPLICATE INVOICE"
    else:
        result = "NEW INVOICE"

        cursor.execute("""
            INSERT INTO invoices
            VALUES (?)
        """, (invoice_number,))

        conn.commit()

    conn.close()

    return result