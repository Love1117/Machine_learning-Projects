import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_device_type, encode_device_ip_reputation, encode_browser,  encode_operating_system, encode_ad_position
from app.core.constants import VPN_USAGE, PROXY_USAGE, WEEKEND
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    device_type_encode = encode_device_type(data.device_type_status)
    device_ip_reputation_encode = encode_device_ip_reputation(data.device_ip_reputation_status)
    browser_encode = encode_browser(data.browser_status)
    operating_system_encode = encode_operating_system(data.operating_system_status)
    ad_position_encode = encode_ad_position(data.ad_position_status)



    input_data = pd.DataFrame([{"click_duration": data.click_duration,
                                "scroll_depth": data.scroll_depth,
                                "mouse_movement": data.mouse_movement,
                                "keystrokes_detected": data.keystrokes_detected,
                                "click_frequency": data.click_frequency,
                                "time_since_last_click": data.time_since_last_click,
                                "VPN_usage": VPN_USAGE[data.VPN_usage],
                                "proxy_usage": PROXY_USAGE[data.proxy_usage],
                                "bot_likelihood_score": data.bot_likelihood_score,
                                "year": data.year,
                                "month": data.month,
                                "day": data.day,
                                "days_of_the_week": data.days_of_the_week,
                                "hour": data.hour,
                                "weekend": WEEKEND[data.weekend],
                                **device_type_encode,
                                **device_ip_reputation_encode,
                                **browser_encode,
                                **operating_system_encode,
                                **ad_position_encode}])


    scaled_df = scale.transform(input_data)


    probability = model.predict(scaled_df)[0][0]
    prediction_class = 1 if probability >= 0.5 else 0


    db_obj = save_prediction(db, data, prediction_class, probability)

    return {
        "prediction_probability": float(probability),
        "is_fraudulent": "Yes" if prediction_class == 1 else "No",
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
