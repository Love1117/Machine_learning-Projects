import spacy
import pytextrank

#load model
model = spacy.load("en_core_web_sm")

# Add TextRank into spaCy pipeline
model.add_pipe("textrank")
