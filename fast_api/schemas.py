from pydantic import BaseModel, EmailStr
from enum import Enum
from database import Roles


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Roles
    group: str | None = None
    disabled: bool = False


class CreateOlympiad(BaseModel):
    name: str


class CreateLocalOlympiad(CreateOlympiad):
    group: str


class CreateGlobalOlympiad(CreateOlympiad):
    group: None
