from pydantic import BaseModel, Field
from datetime import datetime


class FiltrationSchema(BaseModel):
    limit: int = Field(ge=0, default=100)
    event_date_start: datetime = Field(..., example=datetime(2020, 1, 1, 0, 0))
    event_date_end: datetime = Field(..., example=datetime(2030, 1, 1, 0, 0))
