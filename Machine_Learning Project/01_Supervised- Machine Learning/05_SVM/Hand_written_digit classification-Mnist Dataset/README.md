<img width="685" height="216" alt="image" src="https://github.com/user-attachments/assets/167fea0b-ba3c-42e5-9286-d596317c7bba" />





# Hand-Written Digit Classification using SVC

**📘 Project Overview**:

*This project focuses on building a highly accurate machine learning model to automatically recognize and classify hand-written digits (0-9) from image data. This is a fundamental problem in computer vision and the basis for Optical Character Recognition (OCR) systems. The project includes a FastAPI backend, an interactive Streamlit frontend, Docker support, and a trained machine learning model for real-time predictions.*

Project Aim: The primary aim was to develop a robust classification model capable of distinguishing between the ten unique digits

# Technologies Used
*Python,
Scikit-learn,
Pandas,
Matplotlib,
NumPy,
FastAPI,
Streamlit,
PostgreSQL,
SQLAlchemy,
Pydantic,
Docker & Docker Compose,
Uvicorn,
Joblib,
Git & GitHub*

# Features
*Predicts Hand_written_digit using a trained Machine Learning model
Interactive Streamlit web interface
FastAPI REST API for real-time predictions
PostgreSQL database for storing prediction history
SQLAlchemy ORM for database operations
Dockerized application for consistent deployment
Input validation with Pydantic*




# Project structure
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



 # Installation Guide
 
1. Clone the repository
git clone https://github.com/YourUsername/Machine_learning-Projects.git
2. Navigate to the project
cd Machine_learning-Projects/Machine_Learning_Project/01_Supervised-_Machine_Learning/05_SVM/Hand_written_digit classification-Mnist Dataset

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
