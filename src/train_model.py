import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("data/parking_data.csv")

df = pd.get_dummies(df, columns=["location"], drop_first=True)

X = df.drop("parking_available", axis=1)
y = df["parking_available"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print(f"Model accuracy: {accuracy:.2f}")

joblib.dump(model, "models/parking_model.pkl")

print("Model saved.")