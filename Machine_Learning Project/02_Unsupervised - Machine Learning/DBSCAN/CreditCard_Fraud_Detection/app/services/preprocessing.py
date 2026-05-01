def encode_type(type_status):
  return {"type_CASH_OUT": 1 if type_status == "CASH_OUT" else 0,
           "type_DEBIT": 1 if type_status == "DEBIT" else 0,
           "type_PAYMENT": 1 if type_status == "PAYMENT" else 0,
           "type_TRANSFER": 1 if type_status == "TRANSFER" else 0}
