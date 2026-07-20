FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# working directory
WORKDIR /app

COPY requirements.txt .

#pip upgrade and Installing dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copying entire project
COPY . .

# Expose FastAPI and streamlit port
EXPOSE 8000
EXPOSE 8501
