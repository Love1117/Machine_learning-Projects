<img width="686" height="386" alt="image" src="https://github.com/user-attachments/assets/1de3cf5c-c939-4c5a-a4f5-5029af198bf8" />


## Spotify Music Recommendation System Using Cosine Similarity


## Project Overview:

This project implements a content-based music recommendation system using text vectorization and cosine similarity. 
### When deployed, this recommendation system can:
*Recommend songs with similar styles, moods, or characteristics in real time.
Improve user engagement and listening experience on music platforms. 
Serve as a scalable recommendation module for streaming services, playlists, or AI-driven entertainment applications.*

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
*recommend similar music based on their titles.
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
cd Machine_learning-Projects/Machine_Learning_Project/05_Advanced Project_AI/Recommendation System/Music_Recommendation_System


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
