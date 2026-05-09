from transformers import AutoTokenizer, AutoModelForSequenceClassification


model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
roberta_tokenizer = AutoTokenizer.from_pretrained(model_name)
roberta_model = AutoModelForSequenceClassification.from_pretrained(model_name)
print("Roberta model loaded successfully.")
