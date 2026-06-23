import pandas as pd

print("\nAUDITPILOT AI")
print("-------------------")

transactions = pd.read_csv("data/transactions_data.csv")

print(f"Dataset Loaded Successfully")

print(f"Total Records: {len(transactions)}")

print("\nColumns:")

for column in transactions.columns:
    print("-", column)