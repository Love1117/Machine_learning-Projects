<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/116d7e99-1476-4b4a-b8a6-8e5d63c5b8f7" />



## Wod with similar meaning using gensim


## Project Overview:

This project applies gensim to predict words with similar meaning and give word similarity score. 



## Technologies Used
*Python
gensim
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
*Using gensim to predict words with similar meaning.
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
cd Machine_learning-Projects/Machine_Learning_Project/04_NLP Projects/Word2Vec Embeddings/Building Words with Similar meaning



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
