import sys
import json
from pathlib import Path

sys.path.append("src")

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import mlflow
import mlflow.sklearn
from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, ColSpec
import matplotlib.pyplot as plt
import seaborn as sns

from config.config import config


def train_model():
    """Trains the model, logs with MLflow, and saves the model."""
    with mlflow.start_run():
        mlflow.log_params(config["train"])

        df = pd.read_csv(config["data"]["processed_data_path"])
        X = df.drop(columns=["target"])
        y = df["target"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=config["data"]["test_size"],
            random_state=config["base"]["random_state"],
        )

        model = LogisticRegression(C=config["train"]["C"])
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        mlflow.log_metric("accuracy", accuracy)
        print(f"Accuracy: {accuracy}")

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        metrics = {"accuracy": accuracy}
        with open(reports_dir / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=4)
        print(f"Metrics saved to {reports_dir / 'metrics.json'}")

        # Log confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(10, 7))
        sns.heatmap(cm, annot=True, fmt="d")
        plt.xlabel("Predicted")
        plt.ylabel("Truth")
        plt.title("Confusion Matrix")
        plt.savefig("confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png", "plots")

        joblib.dump(model, config["train"]["model_path"])
        print(f"Model saved to {config['train']['model_path']}")

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
            signature=signature,
        )
        print("Model logged to MLflow with a manually defined, robust signature.")


if __name__ == "__main__":
    train_model()
