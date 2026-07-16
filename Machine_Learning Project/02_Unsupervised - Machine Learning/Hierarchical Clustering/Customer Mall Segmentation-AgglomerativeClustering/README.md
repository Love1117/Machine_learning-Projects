<img width="1024" height="731" alt="image" src="https://github.com/user-attachments/assets/17035fb7-74db-4cf9-ae4e-9cca330ec1e8" />



# Customer Mall Segmentation using Agglomerative Clustering

**📘 Project Overview**:

*The main aim is to analyze customer data and group similar customers together based on thier behavior (annual income and spending score), to support targeted marketing strategies, improve customer retention, and enhance decision-making for personalized product recommendations.




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
*Predicts Customer Mall Segmentation using a unsupervised trained Machine Learning model
Interactive Streamlit web interface
FastAPI REST API for real-time predictions
PostgreSQL database for storing prediction history
SQLAlchemy ORM for database operations
Dockerized application for consistent deployment
Input validation with Pydantic*


📊 Results & Insights:
The clustering visualization revealed five distinct customer groups such as:

High-income, high-spending customers

High-income, low-spending customers

Low-income, high-spending customers

Low-income, low-spending customers

Average-income, moderate-spending customers




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
cd Machine_learning-Projects/Machine_Learning_Project/02_Unsupervised - Machine Learning/Hierarchical Clustering/Customer Mall Segmentation-AgglomerativeClusterings

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
