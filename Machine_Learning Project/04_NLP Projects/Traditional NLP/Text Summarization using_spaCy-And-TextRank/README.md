<img width="1000" height="579" alt="image" src="https://github.com/user-attachments/assets/ea2095b6-4185-415e-a043-fa5a78ba7bac" />


## Text Summarization Using spaCy and PyTextRank


## Project Overview:

This project implements an extractive text summarization system using spaCy for natural language processing and PyTextRank for ranking key phrases and sentences. After processing the input text, the model identifies the most important concepts and extracts the most relevant sentences to form a concise summary.


## 🎯 Aim of the Project:

The primary objectives of the project are:
• To build an efficient and lightweight summarization tool capable of condensing long documents into clear, meaningful summaries.


## Technologies Used
*Python
Scikit-learn
Pandas
NumPy
spacy
pytextrank
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
*Summarizing text using spaCy+TextRank.
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
cd Machine_learning-Projects/Machine_Learning_Project/04_NLP Projects/Traditional NLP/Text Summarization using_spaCy+TextRank




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
