# Step 1: Use a lightweight base image
FROM python:3.11-slim as base

# Step 2: Set environment variables for Poetry
ENV POETRY_VERSION=1.7.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Step 5: Set work directory
WORKDIR /app

# Step 6: Copy poetry.lock* and pyproject.toml for dependency caching
COPY ./app/pyproject.toml ./app/poetry.lock* /app/

# Step 7: Install dependencies
RUN poetry install --no-dev --no-root

# Step 8: Copy application source code and data
COPY ./app /app

# Step 9: Run model.py script (for model training)
RUN python /app/model.py
