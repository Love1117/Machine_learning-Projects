from pydantic import BaseModel, Field

class TextRequest(BaseModel):
  text: str = Field(..., example="Think of it as an intro to Disney magic for the little ones. Almost all of the attractions can be completed in 1.5days.One drawback was the timing. For example, Disney's Storybook Theatre is closed Wed Thu for private events. Some restaurants close mid week Tue Thur as well. So best not to plan your visit during mid week.The biggest disappointment is the food at the Park. Even Maxim's is so so only. The only decent Restaurant is Main Street Corner Cafe and the Main Street Bakery. And do be prepared for the typical abrupt HongKong style service from the serving staff.", description="Input text")
