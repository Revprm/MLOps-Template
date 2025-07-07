from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_config():
    """Loads the configuration from params.yaml and validates it."""
    config_path = PROJECT_ROOT / "params.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    if config is None:
        raise ValueError(f"Configuration file is empty or invalid: {config_path}")

    # --- Configuration Validation ---
    required_keys = ["base", "data", "train"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required key '{key}' in {config_path}")

    return config


config = load_config()
