import pandas as pd
from pathlib import Path
import joblib
import json
import yaml
from sklearn.metrics import accuracy_score, f1_score

def evaluate_model(processed_path, model_path, metrics_file, target_col):
    print("Evaluating model...")
    processed_path = Path(processed_path)
    model_path = Path(model_path)
    metrics_file = Path(metrics_file)
    
    test_df = pd.read_csv(processed_path / "test.csv")
    model = joblib.load(model_path)
    
    X_test = test_df.drop(columns=target_col)
    y_test = test_df[target_col]
    
    predictions = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average='weighted')
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"F1 Score (weighted): {f1:.4f}")
    
    # Save metrics
    metrics_file.parent.mkdir(parents=True, exist_ok=True)
    with open(metrics_file, 'w') as f:
        json.dump({'accuracy': accuracy, 'f1_score_weighted': f1}, f, indent=4)
        
    print(f"Metrics saved to {metrics_file}")

if __name__ == "__main__":
    with open("params.yaml", 'r') as f:
        params = yaml.safe_load(f)
        
    evaluate_model(
        processed_path=params['data']['processed_path'],
        model_path=Path(params['model']['dir']) / "model.joblib",
        metrics_file=params['evaluate']['metrics_file'],
        target_col=params['model']['target_col']
    )