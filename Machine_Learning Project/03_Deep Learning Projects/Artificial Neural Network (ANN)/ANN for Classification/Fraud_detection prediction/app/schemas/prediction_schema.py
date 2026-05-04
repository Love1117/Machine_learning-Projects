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
  days_of_the_week: int= Field(..., example=4, description="days of the week")
  hour: float= Field(..., example=2, description="Which hour")
  weekend: Literal["Yes","No"]
  device_type_status: str= Field(..., example="Mobile", description="Device type")
  device_ip_reputation_status: str= Field(..., example="Good", description="Device ip reputation")
  browser_status: str= Field(..., example="Edge", description="What browser")
  operating_system_status: str= Field(..., example="Linux", description="Operating system")
  ad_position_status: str= Field(..., example="Side", description="ad position")
