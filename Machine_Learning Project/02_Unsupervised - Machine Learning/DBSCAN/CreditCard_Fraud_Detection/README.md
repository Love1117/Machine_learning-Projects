<img width="750" height="450" alt="image" src="https://github.com/user-attachments/assets/a18270e2-2620-4251-b423-f699e028aae7" />


# 💳Credit Card Fraud Detection using DBSCAN Clustering

**📘 Project Overview**:

*An end-to-end Machine Learning application which the primary objective is to develop an unsupervised fraud detection system capable of recognizing abnormal transactions automatically. This helps financial institutions and payment processors detect fraud in real-time, minimize financial losses, and enhance overall transaction security.


# Technologies Used
*Python
Scikit-learn
Pandas
NumPy
FastAPI
Streamlit
PostgreSQL
SQLAlchemy
Pydantic
Docker & Docker Compose
Uvicorn
Joblib
Git & GitHub*

# Features
*Predicts credict card fraud using a trained Machine Learning model
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
cd Machine_learning-Projects/Machine_Learning_Project/02_Unsupervised - Machine Learning/DBSCAN/CreditCard_Fraud_Detection

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
