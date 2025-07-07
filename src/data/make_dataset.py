from typing import NoReturn
from sklearn.datasets import load_iris
from config.config import config


def make_dataset() -> NoReturn:
    """Loads the raw iris dataset and saves it."""
    iris = load_iris(as_frame=True)
    df = iris.frame
    df.to_csv(config["data"]["raw_data_path"], index=False)
    print(f"Raw dataset created and saved to {config['data']['raw_data_path']}")


if __name__ == "__main__":
    make_dataset()
