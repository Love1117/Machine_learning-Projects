import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    input_data = pd.DataFrame([{"sepal length (cm)": data.sepal_length,
                                "sepal width (cm)": data.sepal_width,
                                "petal length (cm)": data.petal_length,
                                "petal width (cm)": data.petal_width}])
    
    prediction = model.predict(input_data)[0]

    if prediction==0:
      iris_flower = "Setosa"

    elif prediction==1:
      iris_flower = "Versicolor"

    else:
      iris_flower = "Verginca"

    db_obj = save_prediction(db, data, iris_flower)

    return {
        "prediction": iris_flower,
        "db_id": db_obj.id
    }
      
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
