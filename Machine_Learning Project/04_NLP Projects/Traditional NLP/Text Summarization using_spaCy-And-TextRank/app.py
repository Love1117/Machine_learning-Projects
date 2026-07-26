import spacy
import pytextrank
from fastapi import FastAPI
from pydantic import BaseModel

#load model
model = spacy.load("en_core_web_sm")

# Add TextRank into spaCy pipeline
model.add_pipe("textrank")



# Initialize FastAPI app
app = FastAPI()

# Define a request body model
class TextInput(BaseModel):
    text: str
    limit_phrases: int
    limit_sentences: int

@app.post("/summarize")
async def summarize_text(input_data: TextInput):
    """Summarizes the input text using the pre-trained spaCy and PyTextRank model."""
    doc = model(input_data.text)
    summary_sentences = []
    for sent in doc._.textrank.summary(limit_phrases=input_data.limit_phrases, limit_sentences=input_data.limit_sentences):
        summary_sentences.append(str(sent))
    
    return {"summary": " ".join(summary_sentences)}
