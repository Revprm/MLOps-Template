import joblib
import pandas as pd


def predict_model():
    """Loads the trained model and makes a prediction on sample data."""
    model = joblib.load("models/model.joblib")
    sample = pd.DataFrame(
        {
            "sepal_length": [5.1],
            "sepal_width": [3.5],
            "petal_length": [1.4],
            "petal_width": [0.2],
        }
    )
    prediction = model.predict(sample)
    print(f"Prediction for sample {sample.values} is: {prediction}")


if __name__ == "__main__":
    predict_model()
