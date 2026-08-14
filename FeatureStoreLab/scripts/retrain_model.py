import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

print("================================")
print("MODEL RETRAINING")
print("================================")

df = pd.read_csv("../data/customer_features.csv")
df["BillingStatus"] = [0,0,1,0,1,0,0,1]

X = df[["MonthlyDataUsage","AverageCallCount","MonthlyBill","UsageBillingRatio"]]
y = df["BillingStatus"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "../models/model_v2.pkl")
print("Model retraining completed successfully")
