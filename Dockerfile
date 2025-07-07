FROM python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY . /app

EXPOSE 8080

CMD ["python", "src/app/main.py"]