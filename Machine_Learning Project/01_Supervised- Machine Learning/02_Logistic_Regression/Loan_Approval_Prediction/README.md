<img width="739" height="415" alt="image" src="https://github.com/user-attachments/assets/b6350065-4388-469d-9aac-1dc0a6078dd0" />



# Automated Loan Approval Prediction System Using LogisticsRegression

**📘 Project Overview**:

*TThe core objective is to accurately predict the likelihood of a loan application being Approved or Rejected based on an applicant's historical financial and features (e.g. Age, Gender, Education, Income, Employment_experience, Home_ownership, Loan_amount, Loan_intent, Loan_interest_rate, Loan_percent_income, Credit_history_length, Credit_score, Previous_loan_defaults_on_file, Loan_status). The project includes a FastAPI backend, an interactive Streamlit frontend, Docker support, and a trained machine learning model for real-time predictions.*


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
*Predicts Loan_Approval using a trained Machine Learning model
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
cd Machine_learning-Projects/Machine_Learning_Project/01_Supervised-_Machine_Learning/02_Logistic_Regression/Loan_Approval_Prediction
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
