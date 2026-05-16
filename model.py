import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_profit(sales, quantity):

    X = np.array([[sales, quantity]])

    X_scaled = scaler.transform(X)

    pred = model.predict(X_scaled)[0]

    return "High Profit 🚀" if pred == 1 else "Low Profit 📉"