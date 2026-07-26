def encode_type(status_type):
  return {"type_CASH_OUT": 1 if status_type == "CASH_OUT" else 0,
           "type_DEBIT": 1 if status_type == "DEBIT" else 0,
           "type_PAYMENT": 1 if status_type == "PAYMENT" else 0,
           "type_TRANSFER": 1 if status_type == "TRANSFER" else 0}
