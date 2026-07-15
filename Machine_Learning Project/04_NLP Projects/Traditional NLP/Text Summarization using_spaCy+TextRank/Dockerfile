FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# working directory
WORKDIR /app

COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm

# Copying entire project
COPY . .

# Expose FastAPI and streamlit port
EXPOSE 8000
EXPOSE 8501
