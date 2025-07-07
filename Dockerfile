FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && \
    poetry install --only=main --no-interaction --no-ansi

COPY . /app

EXPOSE 8080

CMD ["python", "src/app/main.py"]