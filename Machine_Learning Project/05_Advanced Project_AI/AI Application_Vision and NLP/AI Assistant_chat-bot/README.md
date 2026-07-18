<img width="800" height="418" alt="image" src="https://github.com/user-attachments/assets/aff1ccdd-c2de-4370-97ca-f83bfd854169" />



## Multimodal AI Application (Vision + NLP) Using Google Gemma 3-27B-IT


## Project Overview:

This project integrates Vision and Natural Language Processing within a single AI application powered by Llama 3.2. The system functions as an intelligent assistant capable of interpreting images, responding to audio records and generating high-quality text responses, enabling it to answer questions, describe visual content, and engage in natural, human-like conversation. The result is a flexible multimodal AI tool that demonstrates advanced reasoning across both text, audio and images.


## Technologies Used
*Python
openai
python-multipart
openai
httpx
pillow
nest-asyncio
faster-whisper
streamlit-mic-recorder
python-dotenv
FastAPI
Streamlit
Pydantic
Docker & Docker Compose
Uvicorn
Git & GitHub*



## Features
*deleveped a AI chat-bot using Llama 3.2.
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
cd Machine_learning-Projects/Machine_Learning_Project/05_Advanced Project_AI/AI Application_Vision and NLP/AI Assistant_chat-bot


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
