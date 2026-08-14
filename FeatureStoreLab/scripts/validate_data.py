import pandas as pd
import os

file_path = "../data/billing_data.csv"

print("====================================")
print("TEST RT-001 - Validate Training Data")
print("====================================")

if not os.path.exists(file_path):
    print("FAIL - billing_data.csv does not exist")
    exit()

print("PASS - billing_data.csv exists")

df = pd.read_csv(file_path)
print("\nColumns found:", list(df.columns))

required_columns = ["CustomerID","DataGB","Calls","BillAmount"]
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print("FAIL - Missing columns:", missing_columns)
else:
    print("PASS - All required columns exist")

if df[required_columns].isnull().sum().sum() == 0:
    print("PASS - No missing values")
else:
    print("FAIL - Missing values found")

if df["CustomerID"].duplicated().sum() == 0:
    print("PASS - No duplicate CustomerID")
else:
    print("FAIL - Duplicate CustomerID found")

if (df["DataGB"] < 0).any():
    print("FAIL - Negative DataGB detected")
else:
    print("PASS - DataGB values are valid")

print("\nTotal records:", len(df))
