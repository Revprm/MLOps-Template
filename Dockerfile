# Build stage
FROM python:3.11-slim as builder

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --only=main

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["python", "src/app/main.py"]