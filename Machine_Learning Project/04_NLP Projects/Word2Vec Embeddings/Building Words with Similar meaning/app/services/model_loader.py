import gensim
import os
from pathlib import Path
from app.core.config import MODEL_DIR

word2vec_model = gensim.models.Word2Vec.load(MODEL_DIR / "netflix_text_reviews.model")
