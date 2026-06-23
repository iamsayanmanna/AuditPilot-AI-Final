from invoice_agent import extract_invoice

invoice = extract_invoice(
    "invoices/test_invoice.pdf"
)

print("\nINVOICE DATA")
print("-------------------")

for key, value in invoice.items():

    if key != "raw_text":
        print(f"{key}: {value}")