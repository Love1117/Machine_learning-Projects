<img width="740" height="494" alt="image" src="https://github.com/user-attachments/assets/32958cf7-047c-4d3a-9cd7-80f541b494fe" />


## Product Recommendation System Using Cosine Similarity


## Project Overview:

This project implements a content-based product recommendation system using text vectorization and cosine similarity. 
### When deployed, this recommendation system can:
*Recommend relevant products in real time based on user interests or selected items.
Improve product discovery, cross-selling, and customer engagement on e-commerce platforms.
Support personalized shopping experiences by delivering data-driven recommendations.*

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
*recommend similar product based on their titles.
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
cd Machine_learning-Projects/Machine_Learning_Project/05_Advanced Project_AI/Recommendation System/Product_Recommendation_System


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
