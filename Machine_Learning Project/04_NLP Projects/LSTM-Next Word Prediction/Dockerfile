FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

#pip upgrade and Installing dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copying entire project
COPY . .

# Run FastAPI app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
