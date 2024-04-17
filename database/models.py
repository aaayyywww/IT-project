from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Annotated
from sqlalchemy import ForeignKey
from database.db import Base
from enum import Enum


class Roles(Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"
    developer = "developer"


intpk = Annotated[int, mapped_column(primary_key=True)]


class StudentOlympiadLink(Base):
    __tablename__ = "connections"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    olympiad_id: Mapped[int] = mapped_column(
        ForeignKey("olympiads.id", ondelete="CASCADE")
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str]
    email: Mapped[str | None]
    hashed_password: Mapped[str]
    role: Mapped[Roles] = mapped_column(default=Roles.student)
    group: Mapped[str | None]
    disabled: Mapped[bool] = mapped_column(default=False)

    olympiads = relationship(
        "Olympiad",
        secondary="connections",
        back_populates="users",
        #  cascade="all, delete-orphan",
    )


class Olympiad(Base):
    __tablename__ = "olympiads"

    id: Mapped[intpk]
    name: Mapped[str]
    group: Mapped[str | None]

    users = relationship(
        "User",
        secondary="connections",
        back_populates="olympiads",
        # cascade="all, delete-orphan",
    )
