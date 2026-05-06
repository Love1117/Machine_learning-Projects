def predict_next_words(input_word: str, len_of_words: int, tokenizer, model):
  generated_text = input_word

  for _ in range(len_of_words):
    seq = tokenizer.texts_to_sequences([generated_text])[0]

    if len(seq) < 3:
      seq_to_predict = pad_sequences([seq], maxlen=3, padding='pre')[0]
    else:
      seq_to_predict = seq[-3:]

    seq_to_predict = np.array(seq_to_predict)

    if not seq_to_predict.tolist():
        break

    # seq_to_predict is already a 1D numpy array from pad_sequences
    # It needs to be reshaped to (1, 3) for the model input
    if seq_to_predict.shape[0] != 3:
        seq_to_predict = pad_sequences([seq_to_predict], maxlen=3, padding='pre')[0]

    seq_to_predict = seq_to_predict.reshape(1, 3)

    # To Ensure model is loaded
    if model is None:
        return "Error: Model not loaded."

    pred_probs = model.predict(seq_to_predict, verbose=0)
    pred_index = np.argmax(pred_probs, axis=1)[0]

    next_word = ""
    next_word_found = False

    for win, idx in tokenizer.word_index.items():
      if idx == pred_index:
        next_word = win
        next_word_found = True
        break

    if next_word_found:
      generated_text += " " + next_word
    else:
      print(f"Predicted index {pred_index} not found in tokenizer vocabulary. Stopping prediction.")
      break

  return generated_text
