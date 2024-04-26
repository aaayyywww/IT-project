from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Annotated
from sqlalchemy import ForeignKey
from database.db import Base
from enum import Enum


class Roles(Enum):
    student = "student"
    admin = "admin"
    developer = "developer"


intpk = Annotated[int, mapped_column(primary_key=True)]


class StudentEventLink(Base):
    __tablename__ = "connections"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"))


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str]
    email: Mapped[str | None]
    hashed_password: Mapped[str]
    role: Mapped[Roles] = mapped_column(default=Roles.student)
    disabled: Mapped[bool] = mapped_column(default=False)
    verified: Mapped[bool] = mapped_column(default=True)
    events = relationship(
        "Event",
        secondary="connections",
        back_populates="users",
        lazy="subquery",
    )


"""class Comments(Base):
    __tablename__ = "comments"
    id: Mapped[intpk]

    post: Mapped[str]
    created: Mapped[datetime] = mapped_column(default=datetime.today())
    updated: Mapped[datetime] = mapped_column(default=datetime.today())

    olympiad_id: Mapped[intpk] = mapped_column(
        ForeignKey("olympiads.id", ondelete="CASCADE")
    )
    user_id: Mapped[intpk] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user = relationship("User", backref="comments")
    olympiad = relationship("Olympiad", backref="comments")"""


class Event(Base):  # переименовать хуету
    __tablename__ = "events"

    id: Mapped[intpk]
    name: Mapped[str]
    subject: Mapped[str | None]
    level: Mapped[int | None]
    tour: Mapped[str | None]
    link: Mapped[str | None]
    university: Mapped[str | None]
    date_start: Mapped[datetime] = mapped_column(default=datetime.now())
    date_end: Mapped[datetime] = mapped_column(default=datetime.now())

    users = relationship(
        "User",
        secondary="connections",
        back_populates="events",
        lazy="subquery",
    )
