# MLOps Infrastructure Template

This repository provides a template for building scalable and reproducible machine learning pipelines using modern MLOps tools. It demonstrates a complete workflow from data processing and model training to experiment tracking, deployment, and CI/CD.

## Features

  - **DVC**: For data and model versioning. 📦
  - **Poetry**: For dependency management.
  - **MLflow**: For experiment tracking. 🧪
  - **FastAPI**: For serving the model as a REST API. 🚀
  - **GitHub Actions**: For CI/CD automation. 🤖
  - **Modular Structure**: A `src` layout for cleaner, more maintainable code. 📂

## Project Structure

```
├── .dvc                  # DVC metadata and cache
├── .github/workflows     # GitHub Actions CI/CD workflows
│   └── ci.yml
├── config                # Configuration files
│   └── config.py
├── data                  # Data files (tracked by DVC)
│   ├── processed         # Processed data
│   └── raw               # Raw data
├── models                # Trained model artifacts (tracked by DVC)
├── notebooks             # Jupyter notebooks for exploration
├── reports               # Generated reports (e.g., model performance)
├── src                   # Source code for the project
│   ├── __init__.py
│   ├── app               # FastAPI application
│   │   └── main.py
│   ├── data              # Scripts for data handling
│   │   ├── __init__.py
│   │   ├── make_dataset.py
│   │   └── process_data.py
│   └── models            # Scripts for training and prediction
│       ├── __init__.py
│       ├── predict_model.py
│       └── train_model.py
├── tests                 # Test scripts
│   ├── test_data.py
│   └── test_pipeline.py
├── .gitignore            # Files and directories to ignore in Git
├── dvc.yaml              # DVC pipeline definition
├── params.yaml           # Parameters for the DVC pipeline
├── poetry.lock           # Exact versions of dependencies
├── pyproject.toml        # Project metadata and dependencies for Poetry
└── README.md             # This file
```

## Getting Started

### Prerequisites

  - Python 3.11+
  - Poetry
  - DVC

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd mlops-infra-template
    ```
2.  **Install dependencies using Poetry:**
    ```bash
    poetry install
    ```
    This command will create a virtual environment and install all the necessary packages.

## Usage

This project uses DVC to manage the machine learning pipeline, which consists of three main stages defined in `dvc.yaml`: `get_data`, `process_data`, and `train`.

1.  **Reproduce the full pipeline**:
    To run the entire pipeline from data downloading to model training, use:
    ```bash
    poetry run dvc repro
    ```
2.  **Running individual scripts**:
    You can also run the Python scripts individually:
      - `python -m src.data.make_dataset`
      - `python -m src.data.process_data`
      - `python -m src.models.train_model`

## Experiment Tracking with MLflow

This project uses MLflow to log experiment parameters, metrics, and models.

To view your experiments, start the MLflow UI:

```bash
mlflow ui
```

This will start a local server, typically at `http://localhost:5000`.

## Deployment as a REST API

A FastAPI application is included to serve the trained model as a REST API.

To run the API:

```bash
poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 8080
```

You can then send POST requests to the `/predict` endpoint. Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8080/predict" \
-H "Content-Type: application/json" \
-d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

## Testing

Tests are in the `tests/` directory and can be run with pytest:

```bash
poetry run pytest
```

## CI/CD

The GitHub Actions workflow in `.github/workflows/ci.yml` is triggered on every push and pull request to the main branch. It automates testing, code formatting checks, and Docker image builds.

## Contributing

Contributions are welcome\! Please feel free to submit a pull request.