import pandas as pd
import joblib

print("========================================")
print("TEST RT-010 - Compare Model V1 vs V2")
print("========================================")

model_v1 = joblib.load("../models/model_v1.pkl")
model_v2 = joblib.load("../models/model_v2.pkl")

test_data = pd.DataFrame({
    "MonthlyDataUsage":[8,12,19,20],
    "AverageCallCount":[110,130,185,180],
    "MonthlyBill":[650,900,1480,1500],
    "UsageBillingRatio":[0.0123,0.0130,0.0128,0.0133]
})

prediction_v1 = model_v1.predict(test_data)
prediction_v2 = model_v2.predict(test_data)

print("\nModel V1 Predictions:", prediction_v1)
print("Model V2 Predictions:", prediction_v2)

differences = prediction_v1 != prediction_v2
print("\nPrediction differences:", differences)

if differences.any():
    print("PASS - Model behavior changed after retraining")
else:
    print("INFO - Predictions unchanged (not failure)")
