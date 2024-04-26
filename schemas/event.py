from pydantic import BaseModel, EmailStr, validator
from database import models
from datetime import datetime


class EventSchema(BaseModel):
    name: str
    subject: str | None = None
    level: int | None = None
    tour: str | None = None
    link: str | None = None
    university: str | None = None
    date_start: datetime = datetime.today().strftime("%Y-%m-%d %H:%M")
    date_end: datetime = datetime.today().strftime("%Y-%m-%d %H:%M")
