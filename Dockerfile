# Start from an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system deps (optional, but good to ensure pip works well)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Default command (can be overridden)
CMD ["python", "main.py"]
