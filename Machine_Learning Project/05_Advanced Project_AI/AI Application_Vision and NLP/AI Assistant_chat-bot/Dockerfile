FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# working directory
WORKDIR /app

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying entire project
COPY . .

# Expose FastAPI and streamlit port
EXPOSE 8000
EXPOSE 8501
