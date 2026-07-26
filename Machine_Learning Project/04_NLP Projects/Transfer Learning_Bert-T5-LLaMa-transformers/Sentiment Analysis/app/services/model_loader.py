from transformers import AutoTokenizer, AutoModelForSequenceClassification


model_name = "distilbert-base-uncased-finetuned-sst-2-english"roberta_tokenizer = AutoTokenizer.from_pretrained(model_name)
Distilbert_model = AutoModelForSequenceClassification.from_pretrained(model_name)
print("Roberta model loaded successfully.")
