FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying entire project
COPY . .

# Expose FastAPI and streamlit port
EXPOSE 8000
EXPOSE 8501
