import pandas as pd
import random

# Program start হওয়ার সময় একবারই load হবে
transactions = pd.read_csv(
    "data/transactions_data.csv",
    nrows=50000
)

transactions["amount"] = (
    transactions["amount"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

suspicious = transactions[
    transactions["amount"] < 0
]

def generate_case():

    sample = suspicious.sample(1)

    amount = float(sample.iloc[0]["amount"])

    case = {
        "case_id": f"AP-2026-{random.randint(1000,9999)}",
        "client_id": int(sample.iloc[0]["client_id"]),
        "merchant_id": int(sample.iloc[0]["merchant_id"]),
        "amount": amount,
        "date": sample.iloc[0]["date"],
        "use_chip": str(sample.iloc[0]["use_chip"]),
        "errors": (
            "NONE"
            if pd.isna(sample.iloc[0]["errors"])
            else str(sample.iloc[0]["errors"])
        )
    }

    return case