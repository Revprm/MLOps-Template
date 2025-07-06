# MLOps Infrastructure Template

This repository provides a template for building scalable and reproducible machine learning pipelines using modern MLOps tools. It demonstrates a complete workflow from data processing and model training to experiment tracking and CI/CD.

## Features

  - **DVC**: For data and model versioning.
  - **Poetry**: For dependency management.
  - **MLflow**: For experiment tracking.
  - **GitHub Actions**: For CI/CD automation.
  - **Modular Structure**: A `src` layout for cleaner, more maintainable code.

## Project Structure

```
├── data
│   ├── processed
│   └── raw
├── models
├── notebooks
├── src
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── make_dataset.py
│   │   └── process_data.py
│   └── models
│       ├── __init__.py
│       ├── predict_model.py
│       └── train_model.py
├── tests
│   └── test_data.py
├── .dvc
├── .github
│   └── workflows
│       └── ci.yml
├── .gitignore
├── dvc.yaml
├── params.yaml
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Getting Started

### Prerequisites

  - Python 3.11+
  - Poetry
  - DVC

### Installation

1.  Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd ml-infra-template
    ```
2.  Install dependencies using Poetry:
    ```bash
    poetry install
    ```

This command will create a virtual environment and install all the necessary packages listed in `pyproject.toml`.

## Usage

This project uses DVC to manage the machine learning pipeline. The pipeline consists of three main stages defined in `dvc.yaml`: `get_data`, `process_data`, and `train`.

1.  **Reproduce the full pipeline**:
    To run the entire pipeline from data downloading to model training, use the following command:
    ```bash
    poetry run dvc repro
    ```
2.  **Running individual scripts**:
    You can also run the Python scripts individually:
      * To create the dataset: `python src/data/make_dataset.py`
      * To process the data: `python src/data/process_data.py`
      * To train the model: `python src/models/train_model.py`

## Experiment Tracking with MLflow

This project uses MLflow to log experiment parameters, metrics, and models.

To view your experiments, start the MLflow UI:

```bash
mlflow ui
```

This will start a local server, typically at http://localhost:5000, where you can view and compare your runs.

## Testing

Tests are located in the `tests/` directory and can be run using pytest:

```bash
poetry run pytest
```

The tests will check the data shape and model accuracy.

## CI/CD

This repository includes a GitHub Actions workflow for continuous integration. The workflow, defined in `.github/workflows/ci.yml`, is triggered on every push and pull request to the main branch. It performs the following steps:

1.  Checks out the repository
2.  Sets up Python
3.  Installs dependencies
4.  Checks code formatting with Black
5.  Reproduces the DVC pipeline
6.  Runs tests with pytest

## Contributing

Contributions are welcome\! Please feel free to submit a pull request.
