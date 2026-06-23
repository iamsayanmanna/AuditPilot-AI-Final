import sqlite3

conn = sqlite3.connect("auditpilot.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM investigations"
)

rows = cursor.fetchall()

print("\nINVESTIGATION HISTORY")
print("--------------------------")

for row in rows:
    print(row)

conn.close()