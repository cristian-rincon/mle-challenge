# Step 1: Use a lightweight base image
FROM python:3.11-slim AS base

# Step 2: Set environment variables for Poetry
ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Step 5: Set work directory
WORKDIR /

# Step 6: Copy poetry.lock* and pyproject.toml for dependency caching
COPY ./pyproject.toml ./poetry.lock* /

# Step 7: Copy application source code and data
COPY ./app /app

# Step 8: Install dependencies
RUN poetry install --no-dev

# Step 9: Run model.py script (for model training)
RUN python /app/model.py

# Final Stage: Running the FastAPI app (this stage is only used if not using docker-compose)
FROM base AS final

# Expose the port for FastAPI
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app.api:loans_api", "--host", "0.0.0.0", "--port", "8000"]