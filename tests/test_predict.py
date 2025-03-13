# tests/test_predict.py
import pytest
import joblib
from src.predict import predict
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def test_predict():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split data into training and testing sets
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForestClassifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)  # Fit the model

    # Save the trained model
    joblib.dump(model, "model.pkl")

    # Test prediction
    input_data = [[5.1, 3.5, 1.4, 0.2]]  # Example input
    prediction = predict(input_data)

    # Check if prediction is not None
    assert prediction is not None, "Prediction should not be None"
