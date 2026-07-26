from fastapi import HTTPException
import torch
from scipy.special import softmax
from app.services.model_loader import roberta_tokenizer, roberta_model
from app.database.crud import save_prediction


def prediction(request, db):
  try:
    inputs = roberta_tokenizer(request.text, truncation=True, padding=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
        outputs = roberta_model(**inputs)

    logits = outputs.logits[0].detach().numpy()
    scores = softmax(logits)

    rob_dict = {"Roberta_neg": float(scores[0]),
                "Roberta_neu": float(scores[1]),
                "Roberta_pos": float(scores[2]),
               }

    db_obj = save_prediction(db, "model": "Roberta", request, "sentiment_scores": rob_dict)

    return {
        "model": "Roberta", 
        "text": request.text, 
        "sentiment_scores": rob_dict,
        "db_id": db_obj.id}
    
   except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
