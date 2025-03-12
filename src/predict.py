import joblib

#A script to make predictions using the trained model
def predict(input_data):
    # Load model
    model = joblib.load("model.pkl")
    return model.predict(input_data)

if __name__ == "__main__":
    # Example input
    input_data = [[5.1, 3.5, 1.4, 0.2]]
    prediction = predict(input_data)
    print(f"Prediction: {prediction}")