import pandas as pd


def process_data():
    """Reads raw data, processes it, and saves the result."""
    df = pd.read_csv("data/raw/iris.csv")

    # Process: clean up column names
    df.columns = [col.replace(" (cm)", "").replace(" ", "_") for col in df.columns]

    # Save processed data
    df.to_csv("data/processed/processed_iris.csv", index=False)
    print("Processed data saved to data/processed/processed_iris.csv")


if __name__ == "__main__":
    process_data()
