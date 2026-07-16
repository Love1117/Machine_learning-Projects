<img width="927" height="331" alt="image" src="https://github.com/user-attachments/assets/9a0b092c-ad34-41a6-a74b-79fb0cc4131c" />




# 🧠 Customer Churn Prediction using Artificial Neural Network (ANN)

**📘 Project Overview**:

*This project uses a Deep Learning Artificial Neural Network (ANN) to predict customer churn — that is, whether a customer is likely to stop or continue using a company’s services.

# 🎯 Aim of the Project:

The main aim is to build an intelligent system that predicts customer churn in advance, allowing businesses to take proactive actions such as offering discounts, improving customer service, or launching retention campaigns to reduce customer loss.


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
*Predicts Customer Churn using a trained Machine Learning model
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
cd Machine_learning-Projects/Machine_Learning_Project/03_Deep Learning Projects/Artificial Neural Network-ANN/ANN for Classification/Customer_churn_prediction

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
