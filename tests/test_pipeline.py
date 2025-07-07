import os
from subprocess import run
import pandas as pd
from config.config import config


def test_pipeline_reproducibility():
    """Tests if the DVC pipeline runs successfully."""
    result = run(["dvc", "repro", "--force"], capture_output=True, text=True)
    assert result.returncode == 0, "DVC pipeline failed to reproduce."
    assert os.path.exists(config["data"]["processed_data_path"])
    assert os.path.exists(config["train"]["model_path"])


def test_prediction_script():
    """Tests the prediction script."""
    result = run(
        ["python", "src/models/predict_model.py"], capture_output=True, text=True
    )
    assert "Prediction for sample" in result.stdout
