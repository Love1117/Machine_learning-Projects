from app.core.constants import Fuel_Columns, Owner_Columns, Seller_type_Columns

def encode_fuel(fuel: str):
    return {col: 1 if col == f"fuel_{fuel}" else 0 for col in Fuel_Columns}

def encode_owner(owner: str):
    return {col: 1 if col == f"owner_{owner}" else 0 for col in Owner_Columns}

def encode_seller_type(seller_type: str):
    return {col: 1 if col == f"seller_type_{seller_type}" else 0 for col in Seller_type_Columns}
