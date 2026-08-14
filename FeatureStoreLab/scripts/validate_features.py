import pandas as pd

print("======================================")
print("TEST RT-003 - Validate Feature Store")
print("======================================")

file_path = "../data/customer_features.csv"
df = pd.read_csv(file_path)

required_features = ["CustomerID","MonthlyDataUsage","AverageCallCount","MonthlyBill","UsageBillingRatio"]

missing = [col for col in required_features if col not in df.columns]
if missing:
    print("FAIL - Missing features:", missing)
else:
    print("PASS - All features exist")

if df[required_features].isnull().sum().sum() == 0:
    print("PASS - No missing feature values")
else:
    print("FAIL - Missing feature values found")

print("\nFeature Store Preview:")
print(df.head())
