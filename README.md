# MLOps Infrastructure Template

This repository provides a template for building scalable and reproducible machine learning pipelines using modern MLOps tools.

## Features

- **DVC**: For data and model versioning.
- **Poetry**: For dependency management.
- **MLflow**: For experiment tracking.
- **GitHub Actions**: For CI/CD automation.
- **Modular Structure**: A `src` layout for cleaner, more maintainable code.

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd ml-infra-template
    ```

2.  **Install dependencies:**
    ```bash
    poetry install
    ```

3.  **Run the DVC pipeline:**
    ```bash
    poetry run dvc repro
    ```

4.  **Start the MLflow UI to view experiments:**
    ```bash
    mlflow ui
    ```