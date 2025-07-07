from typing import NoReturn
import pandas as pd
from config.config import config


def process_data() -> NoReturn:
    """Reads raw data, processes it, and saves the result."""
    df = pd.read_csv(config["data"]["raw_data_path"])
    df.columns = [col.replace(" (cm)", "").replace(" ", "_") for col in df.columns]
    df.to_csv(config["data"]["processed_data_path"], index=False)
    print(f"Processed data saved to " f"{config['data']['processed_data_path']}")


if __name__ == "__main__":
    process_data()
