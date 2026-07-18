<img width="297" height="170" alt="image" src="https://github.com/user-attachments/assets/31800f7d-72d0-48ef-89cb-ea7971fbca44" />



## Movie Recommendation System Using Cosine Similarity


## Project Overview:

This project implements a content-based movie recommendation system using text vectorization and cosine similarity. 
When deployed, this recommendation system can:
Suggest similar movies based on user interests or selected titles. 
Improve user engagement and personalization in entertainment platforms. 
Serve as a foundation for scalable recommendation engines in streaming, e-commerce, or content discovery applications.

## Technologies Used
*Python
FastAPI
Streamlit
Pydantic
Docker & Docker Compose
Uvicorn
Joblib
Git & GitHub*



## Features
*recommend similar movies based on their titles.
Interactive Streamlit web interface
FastAPI REST API for real-time predictions
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
cd Machine_learning-Projects/Machine_Learning_Project/05_Advanced Project_AI/Recommendation System/Movies_Recommendation_System


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
