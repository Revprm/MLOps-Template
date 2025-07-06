import sys

sys.path.append("src")

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn
from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, ColSpec


def train_model():
    """Trains the model, logs with MLflow, and saves the model."""
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    with mlflow.start_run():
        mlflow.log_params(params["train"])

        data_path = "data/processed/processed_iris.csv"
        df = pd.read_csv(data_path)
        X = df.drop(columns=["target"])
        y = df["target"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=params["train"]["test_size"],
            random_state=params["train"]["random_state"],
        )

        model = LogisticRegression(C=params["train"]["C"])
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        mlflow.log_metric("accuracy", accuracy)
        print(f"Accuracy: {accuracy}")

        model_path = "models/model.joblib"
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")

        input_schema = Schema(
            [
                ColSpec("float", "sepal_length"),
                ColSpec("float", "sepal_width"),
                ColSpec("float", "petal_length"),
                ColSpec("float", "petal_width"),
            ]
        )
        output_schema = Schema([ColSpec("integer", "target")])

        signature = ModelSignature(inputs=input_schema, outputs=output_schema)

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            signature=signature,  # Use the manually defined signature
        )
        print("Model logged to MLflow with a manually defined, robust signature.")


if __name__ == "__main__":
    train_model()
