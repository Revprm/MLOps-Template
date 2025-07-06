import pytest
import pandas as pd
from pathlib import Path
import yaml
import json
import subprocess

# Before running tests, ensure the DVC pipeline has been executed
@pytest.fixture(scope="session", autouse=True)
def run_dvc_repro(tmpdir_factory):
    # This fixture ensures `dvc repro` is run once per test session
    print("\nRunning `dvc repro` to generate artifacts for testing...")
    subprocess.run(["dvc", "repro"], check=True)
    print("`dvc repro` finished.")

def test_data_files_created():
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)

    raw_data_file = Path(params['data']['raw_path']) / "iris.csv"
    train_data_file = Path(params['data']['processed_path']) / "train.csv"
    test_data_file = Path(params['data']['processed_path']) / "test.csv"
    model_file = Path(params['model']['dir']) / "model.joblib"
    metrics_file = Path(params['evaluate']['metrics_file'])

    assert raw_data_file.exists(), "Raw data file not found."
    assert train_data_file.exists(), "Train data file not found."
    assert test_data_file.exists(), "Test data file not found."
    assert model_file.exists(), "Model file not found."
    assert metrics_file.exists(), "Metrics file not found."

def test_train_test_split_ratio():
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)

    processed_path = Path(params['data']['processed_path'])
    train_df = pd.read_csv(processed_path / "train.csv")
    test_df = pd.read_csv(processed_path / "test.csv")
    
    total_rows = len(train_df) + len(test_df)
    test_ratio = len(test_df) / total_rows
    
    expected_ratio = params['process']['test_split']
    
    # Check if the actual ratio is close to the expected ratio
    assert abs(test_ratio - expected_ratio) < 0.02

def test_column_consistency():
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)
        
    processed_path = Path(params['data']['processed_path'])
    train_df = pd.read_csv(processed_path / "train.csv")
    test_df = pd.read_csv(processed_path / "test.csv")
    
    assert list(train_df.columns) == list(test_df.columns)

def test_model_performance():
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)
        
    metrics_file = Path(params['evaluate']['metrics_file'])
    
    with open(metrics_file, 'r') as f:
        metrics = json.load(f)
        
    assert metrics['accuracy'] > 0.9, "Model accuracy is below the 0.9 threshold."