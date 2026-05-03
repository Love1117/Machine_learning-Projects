def encode_PaymentMethod(PaymentMethod_status):
        return {"PaymentMethod_Credit card (automatic)": 1 if PaymentMethod_status == "Credit card (automatic)" else 0,
                "PaymentMethod_Electronic check": 1 if PaymentMethod_status == "Electronic check" else 0,
                "PaymentMethod_Mailed check": 1 if PaymentMethod_status == "Mailed check" else 0}

def encode_Contract(Contract_status):
        return {"Contract_One year": 1 if Contract_status == "One year" else 0,
                "Contract_Two year": 1 if Contract_status == "Two year" else 0}


def encode_InternetService(InternetService_status):
        return {"InternetService_DSL": 1 if InternetService_status == "DSL" else 0,
                "InternetService_Fiber optic": 1 if InternetService_status == "Fiber optic" else 0}
