from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  click_duration = Column(Float)
  scroll_depth = Column(Float)
  mouse_movement = Column(Float)
  keystrokes_detected = Column(Integer)
  click_frequency = Column(Float)
  time_since_last_click = Column(Float)
  VPN_usage = Column(String)
  proxy_usage = Column(String)
  bot_likelihood_score = Column(Float)
  year = Column(Integer)
  month = Column(Integer)
  day = Column(Integer)
  days_of_the_week = Column(Integer)
  hour = Column(Float)
  weekend = Column(String)
  device_type_status = Column(String)
  device_ip_reputation_status = Column(String)
  browser_status = Column(String)
  operating_system_status = Column(String)
  ad_position_status = Column(String)
  prediction = Column(String)
  probability = Column(Float)
