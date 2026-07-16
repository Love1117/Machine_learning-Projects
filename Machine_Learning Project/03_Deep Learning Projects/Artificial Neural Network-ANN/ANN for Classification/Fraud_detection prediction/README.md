<img width="846" height="480" alt="image" src="https://github.com/user-attachments/assets/79b9f8dd-4e80-4ace-bc6d-eb6c45fb068c" />


# 🏦Bank Transaction Fraud Detection using Artificial Neural Network (ANN)

**📘 Project Overview**:

*This project applies a Deep Learning Artificial Neural Network (ANN) to detect fraudulent banking transactions by analyzing complex behavioral and transactional patterns.*


# Technologies Used
*Python
Scikit-learn
Pandas
NumPy
FastAPI
Tensorflow
Streamlit
PostgreSQL
SQLAlchemy
Pydantic
Docker & Docker Compose
Uvicorn
Joblib
Git & GitHub*



# Features
*Predicts fraud detection using deep learning (ANN) model
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
cd Machine_learning-Projects/Machine_Learning_Project/03_Deep Learning Projects/Artificial Neural Network-ANN/ANN for Classification/Fraud_detection prediction

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
