import pandas as pd

def match_invoice(amount):

    transactions = pd.read_csv(
        "data/transactions_data.csv"
    )

    transactions["amount"] = (
        transactions["amount"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .astype(float)
    )

    match = transactions[
        transactions["amount"].abs() == amount
    ]

    if len(match) > 0:

        return {
            "status": "MATCH FOUND",
            "risk": "LOW"
        }

    return {
        "status": "NO MATCH FOUND",
        "risk": "HIGH"
    }