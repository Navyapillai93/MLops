import requests

url = "http://127.0.0.1:5000/predict"
payload = [{
    "MonthlyDataUsage":500,
    "AverageCallCount":1500,
    "MonthlyBill":10,
    "UsageBillingRatio":0.015
}]

response = requests.post(url, json=payload)
print("Response:", response.json())
print("Normal Billing" if response == 0 else "Anomaly Detected")
print ("This Billing Anomaly detection system developed by Navya")
