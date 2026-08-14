import os
import joblib

print("================================")
print("TEST RT-009 - Model Verification")
print("================================")

model_path = "../models/model_v2.pkl"

if not os.path.exists(model_path):
    print("FAIL - Model V2 does not exist")
    exit()

print("PASS - Model V2 exists")

try:
    model = joblib.load(model_path)
    print("PASS - Model V2 can be loaded")
    print("Model type:", type(model).__name__)
except Exception as e:
    print("FAIL - Model cannot be loaded")
    print("Error:", e)
