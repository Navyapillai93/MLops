import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

print("================================")
print("Training Model V1")
print("================================")

df = pd.read_csv("C:/Navya/BlobML/data/covid_features.csv")

X = df[["Age","Temperature","HeartRate","OxygenLevel","CoughDays","Comorbidity"]]
y = df[["HighRisk"]]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "../models/model_v2.pkl")
print("Model V1 trained successfully")
