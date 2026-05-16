import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from data_loader import load_data
from analysis import create_target

# Load data
df = load_data()
df = create_target(df)

# Features
features = ["Sales", "Quantity"]

X = df[features]
y = df["ProfitLabel"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Scaling مهم جدًا مع SVM
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# SVM Model
model = SVC(kernel="rbf", C=1, gamma="scale")

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")