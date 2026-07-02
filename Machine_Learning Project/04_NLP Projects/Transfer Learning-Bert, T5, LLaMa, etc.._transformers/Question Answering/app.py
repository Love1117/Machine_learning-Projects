import nest_asyncio
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline



qa_data = {
    "What did Loveday discover about learning?": "From childhood notebooks to the screen of his first computer, Loveday Shadrack discovered he didn’t just love learning—he needed it.",
    "How does Loveday view coding now?": "As he grew, Loveday stopped seeing coding as just a skill. It became a calling that shaped his purpose.",
    "How does Loveday view music?": "Loveday Shadrack never treated music as a mere hobby. It was a part of his soul and a channel for storytelling.",
    "What are the two worlds Loveday Shadrack carries inside him?": "Loveday Shadrack grew up carrying two worlds inside him: one of code, logic, and problem-solving, and another filled with rhythm, melody, and the voice of a storyteller.",
    "What did Loveday realize about greatness?": "Slowly, Loveday realized that greatness wasn’t a single moment but an ongoing journey requiring consistency and growth.",
    "What three things was Loveday sharpening or strengthening as he grew?": "Loveday Shadrack became a young man sharpening his mind, strengthening his spirit, and refining his talents despite challenges.",
    "How did Loveday respond when life felt heavy?": "Even when life felt heavy, Loveday continued pushing forward with determination and faith.",
    "What two fields shaped Loveday’s identity?": "Loveday’s journey combined technology and artistry, allowing him to build a purpose-driven identity.",
    "What qualities guided Loveday into becoming a young man with purpose?": "Loveday Shadrack grew from a curious boy into a young man with purpose, guided by ambition and spiritual strength.",
    "What cannot stop Loveday’s rising journey?": "His story is still unfolding, but it is clear that nothing—no hardship, no doubt, no fear—can stop the man God is shaping him to be.",
}



app = FastAPI()


try:
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")
    print("Question Answering pipeline loaded successfully.")
except NameError:
    print("Error: 'model_link' is not defined. Please run the cell where `model_link` is set (e.g., `model_link = \"deepset/roberta-base-squad2\"`).")
    qa_pipeline = None


class Question(BaseModel):
  question: str


@app.post("/predict/")
async def predict_answer(question_data: Question):
    if qa_pipeline is None:
        return {"error": "Model not loaded"}

    question = question_data.question

    # Auto-pick context
    context = qa_data.get(question)

    if context is None:
        return {"error": "Question not found in database"}

    result = qa_pipeline(question=question, context=context)

    return {
        "question": question,
        "context": context,
        "answer": result["answer"],
        "score": result["score"]
    }
