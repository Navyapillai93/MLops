import pandas as pd
import joblib

print("================================")
print("Model Prediction Test")
print("================================")

model = joblib.load("../models/model_v2.pkl")

customer = pd.DataFrame({
    "Age":[70],
    "Temperature":[130],
    "HeartRate":[50],
    "OxygenLevel":[5],
    "CoughDays": [60],
    "Comorbidity": [4]
})

prediction = model.predict(customer)
print("Prediction:", prediction[0])

if prediction[0] == 0:
    print("Result: Normal fever")
else:
    print("Result: Covid Anomaly Detected")
