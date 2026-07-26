<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/85bfb29b-b3b7-4239-b376-43010ea2f2f9" />


## Sentiment Analysis on Disneyland Reviews Using VADER and Roberta Pre-trained model


## Project Overview:

This project applies the VADER and Roberta to classify customer feedback from the Disneyland Reviews dataset (Kaggle). After preprocessing the review text, both VADER and Roberta effectively categorized each review into positive, neutral, or negative sentiment, capturing both polarity and intensity with strong consistency and interpretability.


## 🎯 Aim of the Project:

*To analyze customer opinions and detect sentiment patterns without the need for heavy model training.
*To demonstrate how VADER and Roberta can deliver fast, actionable sentiment insights from large review datasets.

## Technologies Used
*Python
Pandas
NumPy
spacy
transformers
torch
nltk
FastAPI
Streamlit
PostgreSQL
SQLAlchemy
Pydantic
Docker & Docker Compose
Uvicorn
Joblib
Git & GitHub*



## Features
*Using vader and roberta to effectively categorized each review into positive, neutral, or negative sent.
Interactive Streamlit web interface
FastAPI REST API for real-time predictions
PostgreSQL database for storing prediction history
SQLAlchemy ORM for database operations
Dockerized application for consistent deployment
Input validation with Pydantic*




## Project structure
                   +----------------------+
                   |  Streamlit Frontend  |
                   +----------+-----------+
                              |
                              |
                    HTTP Requests
                              |
                              ▼
                   +----------------------+
                   |    FastAPI Backend   |
                   +----------+-----------+
                              |
          +-------------------+-------------------+
          |                                       |
          ▼                                       ▼
 Machine Learning Model                  PostgreSQL Database
 (Prediction Engine)                  (Stores Predictions)



 ## Installation Guide
 
1. Clone the repository
git clone https://github.com/YourUsername/Machine_learning-Projects.git
2. Navigate to the project
cd Machine_learning-Projects/Machine_Learning_Project/04_NLP Projects/Transfer Learning-Bert, T5, LLaMa, etc.._transformers/Sentiment Analysis




3. Create a virtual environment

~ Windows
python -m venv venv
venv\Scripts\activate

~ Linux/macOS
python3 -m venv venv
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

6. Start the FastAPI server
uvicorn app.main:app --reload

# The API will be available at
http://127.0.0.1:8000

# Swagger Documentation
http://127.0.0.1:8000/docs

6. Start the Streamlit application

Open a new terminal.

streamlit run frontend/streamlit_app.py

The application will open at
http://localhost:8501


# Live Demo For Testing
visit the live demo folder on this app
