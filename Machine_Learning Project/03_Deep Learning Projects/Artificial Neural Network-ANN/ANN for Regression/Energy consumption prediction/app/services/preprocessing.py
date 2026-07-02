def encode_Appliance_Type(Appliance_Type_status):
        return {"Appliance_Type_Computer": 1 if Appliance_Type_status == "Computer" else 0,
                "Appliance_Type_Dishwasher": 1 if Appliance_Type_status == "Dishwasher" else 0,
                "Appliance_Type_Fridge": 1 if Appliance_Type_status == "Fridge" else 0,
                "Appliance_Type_Heater": 1 if Appliance_Type_status == "Heater" else 0,
                "Appliance_Type_Lights": 1 if Appliance_Type_status == "Lights" else 0,
                "Appliance_Type_Microwave": 1 if Appliance_Type_status == "Microwave" else 0,
                "Appliance_Type_Oven": 1 if Appliance_Type_status == "Oven" else 0,
                "Appliance_Type_TV": 1 if Appliance_Type_status == "TV" else 0,
                "Appliance_Type_Washing Machine": 1 if Appliance_Type_status == "Washing Machine" else 0}


def encode_Season(Season_status):
        return {"Season_Spring": 1 if Season_status == "Spring" else 0,
                "Season_Summer": 1 if Season_status == "Summer" else 0,
                "Season_Winter": 1 if Season_status == "Winter" else 0}
