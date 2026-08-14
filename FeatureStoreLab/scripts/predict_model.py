import pandas as pd
import joblib

print("================================")
print("Model Prediction Test")
print("================================")

model = joblib.load("../models/model_v1.pkl")

customer = pd.DataFrame({
    "MonthlyDataUsage":[12],
    "AverageCallCount":[130],
    "MonthlyBill":[900],
    "UsageBillingRatio":[0.013]
})

prediction = model.predict(customer)
print("Prediction:", prediction[0])

if prediction[0] == 0:
    print("Result: Normal Billing")
else:
    print("Result: Billing Anomaly Detected")
