import pandas as pd
from sklearn.linear_model import LogisticRegression
from pathlib import Path
import joblib
import yaml

def train_model(processed_path, model_dir, target_col, seed, C):
    print("Training model...")
    processed_path = Path(processed_path)
    model_dir = Path(model_dir)
    
    train_df = pd.read_csv(processed_path / "train.csv")
    
    X_train = train_df.drop(columns=target_col)
    y_train = train_df[target_col]
    
    # Train model
    model = LogisticRegression(random_state=seed, C=C, max_iter=200)
    model.fit(X_train, y_train)
    
    # Ensure the directory exists
    model_dir.mkdir(parents=True, exist_ok=True)
    model_path = model_dir / "model.joblib"
    
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)
        
    train_model(
        processed_path=params['data']['processed_path'],
        model_dir=params['model']['dir'],
        target_col=params['model']['target_col'],
        seed=params['base']['seed'],
        C=params['train']['C']
    )