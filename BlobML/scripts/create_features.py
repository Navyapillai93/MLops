import pandas as pd
from blob_utils import download_blob, upload_blob

print("=== VODAFONE FEATURE ENGINEERING ===")

download_blob("raw_data/billing_data.csv", "billing_data.csv")
df = pd.read_csv("billing_data.csv")

df["MonthlyDataUsage"] = df["DataGB"]
df["AverageCallCount"] = df["Calls"]
df["MonthlyBill"] = df["BillAmount"]
df["UsageBillingRatio"] = df["DataGB"] / df["BillAmount"]

df.to_csv("customer_features.csv", index=False)
upload_blob("customer_features.csv", "feature_store/customer_features.csv")

print("Feature Store Updated Successfully")
print(df)
