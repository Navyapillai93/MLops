import pandas as pd

print("================================")
print("Creating Feature Store")
print("================================")

df = pd.read_csv("../data/billing_data.csv")

df_features = pd.DataFrame()
df_features["CustomerID"] = df["CustomerID"]
df_features["MonthlyDataUsage"] = df["DataGB"]
df_features["AverageCallCount"] = df["Calls"]
df_features["MonthlyBill"] = df["BillAmount"]
df_features["UsageBillingRatio"] = df["DataGB"] / df["BillAmount"]

df_features.to_csv("../data/customer_features.csv", index=False)
print("Feature Store Created Successfully")
