import pandas as pd
from sklearn.datasets import load_iris
from pathlib import Path
import yaml

def get_data(raw_path):
    print("Fetching Iris dataset...")
    iris = load_iris(as_frame=True)
    df = iris.frame
    
    # Ensure the directory exists
    raw_path = Path(raw_path)
    raw_path.mkdir(parents=True, exist_ok=True)
    
    output_file = raw_path / "iris.csv"
    df.to_csv(output_file, index=False)
    print(f"Dataset saved to {output_file}")

if __name__ == "__main__":
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)
    
    get_data(params['data']['raw_path'])