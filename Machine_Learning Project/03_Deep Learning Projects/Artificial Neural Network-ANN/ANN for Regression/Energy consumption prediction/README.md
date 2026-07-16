<img width="764" height="401" alt="image" src="https://github.com/user-attachments/assets/19068380-7f08-40d3-89d5-94d61355e1a5" />



# Smart Home Energy Consumption Prediction using Artificial Neural Network (ANN)

# 🎯 Aim of the Project:

*The main aim of this project is to develop an intelligent model that predicts future energy consumption in smart homes. This helps homeowners and energy providers to:*

* Monitor and manage energy usage efficiently

* Identify consumption patterns and peak usage hours

* Reduce unnecessary energy costs

* Support sustainability and smart grid initiatives*


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
cd Machine_learning-Projects/Machine_Learning_Project/03_Deep Learning Projects/Artificial Neural Network-ANN/ANN for Regression/Energy consumption prediction

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
