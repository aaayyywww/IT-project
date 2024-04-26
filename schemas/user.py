from pydantic import BaseModel, EmailStr, validator
from database import models


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    role: models.Roles


class RegistrationSchema(UserSchema):
    password: str
