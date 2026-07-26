<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/052ca171-638e-44bc-b156-4f27f67e2b99" />



## Text Generation Using Meta LLaMA 3.2


## Project Overview:

This project showcases a text-generation and conversational AI system built using Meta LLaMA 3.2. The model was implemented as a chatbot capable of generating human-like responses, answering questions, and engaging in open-ended dialogue. 


## Technologies Used
*Python
openai
python-dotenv
FastAPI
Streamlit
Pydantic
Docker & Docker Compose
Uvicorn
Joblib
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
cd Machine_learning-Projects/Machine_Learning_Project/04_NLP Projects/Transfer Learning-Bert, T5, LLaMa, etc.._transformers/Text Generation




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
