from pathlib import Path
import yaml


def load_config():
    """Loads the configuration from params.yaml."""
    config_path = Path(__file__).resolve().parents[1] / "params.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


config = load_config()
