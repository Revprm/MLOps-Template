import pandas as pd
from sklearn.datasets import load_iris


def make_dataset():
    """Loads the raw iris dataset and saves it."""
    iris = load_iris(as_frame=True)
    df = iris.frame
    # Save with original column names
    df.to_csv("data/raw/iris.csv", index=False)
    print("Raw dataset created and saved to data/raw/iris.csv")


if __name__ == "__main__":
    make_dataset()
