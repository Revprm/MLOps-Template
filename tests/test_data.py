import pandas as pd
import joblib
from sklearn.metrics import accuracy_score


def test_data_shape():
    """Tests if the processed data has the expected shape."""
    df = pd.read_csv("data/processed/processed_iris.csv")
    assert df.shape[1] == 5, "Processed data should have 5 columns."


def test_model_accuracy():
    """Tests if the model accuracy is above a certain threshold."""
    model = joblib.load("models/model.joblib")
    df = pd.read_csv("data/processed/processed_iris.csv")
    X = df.drop(columns=["target"])
    y = df["target"]

    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    assert accuracy > 0.9, "Model accuracy should be greater than 0.9."
