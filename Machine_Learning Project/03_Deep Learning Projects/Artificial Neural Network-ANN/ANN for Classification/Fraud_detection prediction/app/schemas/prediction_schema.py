from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  click_duration: float= Field(..., example=0.29, description="Click duration")
  scroll_depth: float= Field(..., example=60, description="Scroll depth")
  mouse_movement: float= Field(..., example=111, description="Mouse movement")
  keystrokes_detected: int= Field(..., example=8, description="What is your monthly charges")
  click_frequency: float= Field(..., example=7, description="Click frequency")
  time_since_last_click: float= Field(..., example=72, description="Time since last click")
  VPN_usage: Literal["Yes","No"]
  proxy_usage: Literal["Yes","No"]
  bot_likelihood_score: float= Field(..., example=0.29, description="Bot likelihood score")
  year: int= Field(..., example=2024, description="What year")
  month: int= Field(..., example=8, description="What month")
  day: int= Field(..., example=23, description="What day")
  days_of_the_week: Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  hour: float= Field(..., example=2, description="Which hour")
  weekend: Literal["Yes","No"]
  device_type_status: Literal["Desktop", "Mobile", "Tablet"]
  device_ip_reputation_status: Literal["Good", "Suspicious", "Bad"]
  browser_status: Literal["Edge", "Firefox", "Opera", "Safari", "Chrome"]
  operating_system_status: Literal["Linux", "iOS", "macOS", "Windows", "Android"]
  ad_position_status: Literal["Side", "Bottom", "Top"]
