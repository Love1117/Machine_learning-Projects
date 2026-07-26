from fastapi import HTTPException
import torch
from scipy.special import softmax
from app.services.model_loader import Distilbert_tokenizer, Distilbert_model
from app.database.crud import save_prediction

def prediction(request, db):
  try:
    inputs = Distilbert_tokenizer(request.text, truncation=True, padding=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
        outputs = DistilBERT_model(**inputs)

    logits = outputs.logits[0].detach().numpy()
    scores = softmax(logits)

    rob_dict = {"Distilbert_neg": float(scores[0]),
                "Distilbert_neu": float(scores[1]),
                "Distilbert_pos": float(scores[2]),
               }

    db_obj = save_prediction(db=db, model="Distilbert", request=request, sentiment_scores=rob_dict)

    return {
        "model": "Distilbert", 
        "text": request.text, 
        "sentiment_scores": rob_dict,
        "db_id": db_obj.id}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
