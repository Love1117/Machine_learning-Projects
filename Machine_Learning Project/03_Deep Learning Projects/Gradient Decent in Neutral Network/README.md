<img width="556" height="359" alt="image" src="https://github.com/user-attachments/assets/768c216f-bc9a-477c-9003-6619c8108ce5" />


# Custom Gradient Descent Implementation for Insurance ownership Prediction

**📘 Project Overview**:

*This project focuses on building a custom Gradient Descent prediction function from scratch — replicating the core learning process of an Artificial Neural Network (ANN). Using only NumPy, a sigmoid activation function, and a weighted sum computation, the model was trained on an insurance dataset containing 8 features (7 input variables and 1 target variable) to know if a customer has insurance or not.*

# 🎯 Aim of the Project:

The main aim is to implement and understand the internal mechanics of gradient descent optimization used in neural networks. By coding the learning process manually, this project deepens the understanding of how machine learning models adjust their parameters to minimize loss and improve prediction accuracy.

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
*Predicts Customer insurance using a build from strach gradient decent model
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
cd Machine_learning-Projects/Machine_Learning_Project/03_Deep Learning Projects/Gradient Decent in Neutral Network

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
