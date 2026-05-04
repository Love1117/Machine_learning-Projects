from app.database.models import Prediction
from app.core.constants import VPN_USAGE, PROXY_USAGE, WEEKEND

def save_prediction(db, data, prediction_class, probability):
  db_obj = Prediction(
        click_duration=data.click_duration,
        scroll_depth=data.scroll_depth,
        mouse_movement=data.mouse_movement,
        keystrokes_detected=data.keystrokes_detected,
        click_frequency=data.click_frequency,
        time_since_last_click=data.time_since_last_click,
        VPN_usage=VPN_USAGE[data.VPN_usage],
        proxy_usage=PROXY_USAGE[data.proxy_usage],
        bot_likelihood_score=data.bot_likelihood_score,
        year=data.year,
        month=data.month,
        day=data.day,
        days_of_the_week=data.days_of_the_week,
        hour=data.hour,
        weekend=WEEKEND[data.weekend],
        device_type_status=data.device_type_status,
        device_ip_reputation_status=data.device_ip_reputation_status,
        browser_status=data.browser_status,
        operating_system_status=data.operating_system_status,
        ad_position_status=data.ad_position_status
        prediction=prediction_class,
        probability=probability
    )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj
