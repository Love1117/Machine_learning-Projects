<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/bc32aaf4-20ac-4d01-a4da-33e01d12700d" />


# 

**📘 Project Overview**:

*This project involves building a fully functional Neural Network from scratch without relying on high-level deep learning frameworks such as TensorFlow or Keras. The model was trained on an insurance dataset containing 8 features — 7 input features (such as age, sex, BMI, children, smoker, region, and charges) and 1 target variable (insurance claim).
The custom-built neural network achieved an impressive 99% accuracy, performing almost identically to a TensorFlow-based ANN model trained on the same data. This demonstrates a deep understanding of the mathematical and computational foundations of neural networks, including forward propagation, backpropagation, weight updates, and activation functions.*

# 🎯 Aim of the Project:

The primary aim of this project is to understand and implement the core architecture of a neural network manually, without using pre-built machine learning libraries. This includes coding every step of the model — from data preprocessing and initialization to loss calculation and gradient updates — to gain a clear understanding of how ANNs learn from data.

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
*Predicts Customer insurance using a build from strach neural network
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
cd Machine_learning-Projects/Machine_Learning_Project/03_Deep Learning Projects/Neutral Network from scratch


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
