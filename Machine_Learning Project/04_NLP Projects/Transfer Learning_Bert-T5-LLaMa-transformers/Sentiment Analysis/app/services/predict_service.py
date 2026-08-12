from fastapi import HTTPException
import torch
from scipy.special import softmax
from app.services.model_loader import Distilbert_tokenizer, Distilbert_model
from app.database.crud import save_prediction

def prediction(request, db):
  try:
    inputs = Distilbert_tokenizer(request.text, truncation=True, padding=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
        outputs = Distilbert_model(**inputs)

    logits = outputs.logits[0].detach().numpy()
    scores = softmax(logits)

    sentiment_score= {"negative": float(scores[0]),
                "positive": float(scores[1])
               }

    predicted_class = torch.argmax(outputs.logits, dim=1).item()

    label = "Positive" if predicted_class == 1 else "Negative"

    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db=db, model="Distilbert", request=request, sentiment_scores=sentiment_score)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass
    

    return {
        "model": "Distilbert", 
        "text": request.text,
        "prediction": label,
        "sentiment_scores": sentiment_score,
        "db_id": db_id,
        "database_saved": database_saved}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
