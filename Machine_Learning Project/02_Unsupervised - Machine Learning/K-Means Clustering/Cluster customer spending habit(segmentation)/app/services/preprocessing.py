def encode_Profession(Profession_status: str):
        return {"Profession_Doctor": 1 if Profession_status == "Doctor" else 0,
                "Profession_Engineer": 1 if Profession_status == "Engineer" else 0,
                "Profession_Entertainment": 1 if Profession_status == "Entertainment" else 0,
                "Profession_Executive": 1 if Profession_status == "Executive" else 0,
                "Profession_Healthcare": 1 if Profession_status == "Healthcare" else 0,
                "Profession_Homemaker": 1 if Profession_status == "Homemaker" else 0,
                "Profession_Lawyer": 1 if Profession_status == "Lawyer" else 0,
                "Profession_Marketing": 1 if Profession_status == "Marketing" else 0}


def encode_Variable(Variable_status: str):
        return {"Var_1_Cat_2": 1 if Variable_status == "cat_2" else 0,
                "Var_1_Cat_3": 1 if Variable_status == "cat_3" else 0,
                "Var_1_Cat_4": 1 if Variable_status == "cat_4" else 0,
                "Var_1_Cat_5": 1 if Variable_status == "cat_5" else 0,
                "Var_1_Cat_6": 1 if Variable_status == "cat_6" else 0,
                "Var_1_Cat_7": 1 if Variable_status == "cat_7" else 0}
