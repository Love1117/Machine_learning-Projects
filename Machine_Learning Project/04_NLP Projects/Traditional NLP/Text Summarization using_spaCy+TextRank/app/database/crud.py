from app.database.models import Prediction

def save_prediction(db, input_data, summary):

    db_obj = Prediction(
    text = Column(String)
    limit_phrases = Column(Integer)
    limit_sentences = Column(Integer)
    summary = Column(String)
