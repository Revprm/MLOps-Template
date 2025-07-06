import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
import yaml

def process_data(raw_path, processed_path, test_split, seed):
    print("Processing data...")
    raw_path = Path(raw_path)
    processed_path = Path(processed_path)
    
    df = pd.read_csv(raw_path / "iris.csv")
    
    # Split data
    train_df, test_df = train_test_split(df, test_size=test_split, random_state=seed)
    
    # Ensure the directory exists
    processed_path.mkdir(parents=True, exist_ok=True)
    
    train_output = processed_path / "train.csv"
    test_output = processed_path / "test.csv"
    
    train_df.to_csv(train_output, index=False)
    test_df.to_csv(test_output, index=False)
    
    print(f"Train set saved to {train_output}")
    print(f"Test set saved to {test_output}")

if __name__ == "__main__":
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)
        
    process_data(
        raw_path=params['data']['raw_path'],
        processed_path=params['data']['processed_path'],
        test_split=params['process']['test_split'],
        seed=params['base']['seed']
    )