FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && rm -rf /root/.cache/pip

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --only=main --no-interaction --no-ansi --no-root \
    && rm -rf /root/.cache/pypoetry \
    && poetry cache clear --all pypi

COPY src /app/src
COPY README.md /app/

RUN poetry install --only-root --no-interaction --no-ansi

EXPOSE 8080

CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8080"]