from transformers import pipeline


try:
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")
    print("Question Answering pipeline loaded successfully.")
except NameError:
    print("Error: 'model_link' is not defined. Please run the cell where `model_link` is set (e.g., `model_link = \"deepset/roberta-base-squad2\"`).")
    qa_pipeline = None
