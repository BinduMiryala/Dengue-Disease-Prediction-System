import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("modified_dataset.csv")  # Ensure this file exists in the same directory
X = data.drop(columns=['RiskLevel'])  # Features
y = data['RiskLevel']  # Target

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE for Handling Imbalance
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_resampled)
X_test_scaled = scaler.transform(X_test)

# Train XGBoost Classifier
model = XGBClassifier()
model.fit(X_train_scaled, y_train_resampled)

# Evaluate Model Accuracy
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the Model and Scaler
joblib.dump(model, "DenguePrediction/model.pkl")
joblib.dump(scaler, "DenguePrediction/scaler.pkl")

print("✅ Model and Scaler saved successfully!")