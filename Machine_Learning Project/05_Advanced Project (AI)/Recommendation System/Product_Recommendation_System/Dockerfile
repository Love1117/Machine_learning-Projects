 FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# working directory
WORKDIR /app

COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying entire project
COPY . .


EXPOSE 8000
EXPOSE 8501
