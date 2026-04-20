from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from scipy.special import softmax


# Initialize FastAPI app
app = FastAPI(title="Disneyland Review Sentiment Analysis API")

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')


# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Load Roberta model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
roberta_tokenizer = AutoTokenizer.from_pretrained(model_name)
roberta_model = AutoModelForSequenceClassification.from_pretrained(model_name)
print("VADER and Roberta models loaded successfully.")


class TextRequest(BaseModel):
  text: str = Field(..., example="Think of it as an intro to Disney magic for the little ones. Almost all of the attractions can be completed in 1.5days.One drawback was the timing. For example, Disney's Storybook Theatre is closed Wed Thu for private events. Some restaurants close mid week Tue Thur as well. So best not to plan your visit during mid week.The biggest disappointment is the food at the Park. Even Maxim's is so so only. The only decent Restaurant is Main Street Corner Cafe and the Main Street Bakery. And do be prepared for the typical abrupt HongKong style service from the serving staff.", description="Input text")


@app.post("/predict-vader")
async def predict_vader_sentiment(request: TextRequest):
  """
  Analyzes the sentiment of the provided text using the VADER model.
  Returns polarity scores (negative, neutral, positive, compound).
  """
  scores = sia.polarity_scores(request.text)
  return {"model": "VADER", "text": request.text, "sentiment_scores": scores}




@app.post("/predict-roberta")
async def predict_roberta_sentiment(request: TextRequest):
    """
    Analyzes the sentiment of the provided text using the Roberta pre-trained model.
    Returns scores for negative, neutral, and positive sentiment.
    """
    inputs = roberta_tokenizer(request.text, truncation=True, padding=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
        outputs = roberta_model(**inputs)

    logits = outputs.logits[0].detach().numpy()
    scores = softmax(logits)

    rob_dict = {"Roberta_neg": float(scores[0]),
                "Roberta_neu": float(scores[1]),
                "Roberta_pos": float(scores[2]),
               }

    return {"model": "Roberta", "text": request.text, "sentiment_scores": rob_dict}
