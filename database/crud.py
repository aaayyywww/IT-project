from sqlalchemy.orm import Session
from database import models
from datetime import datetime, timedelta
from calendar import monthrange, isleap
from fastapi import FastAPI, Depends, HTTPException
import schemas
from routers.auth import pwd_context
from sqlalchemy import select
from typing import List


# def create_olympiad(db: Session):
# def get_events_from_database(
#    db: Session, year: int, month: int | None, day: int | None
# ):
#    if month is None or month == 0:
#        event_start = datetime(year=year, month=1, day=1)
#        event_end = event_start + timedelta(days=365 + 1 * isleap(year + 1))
#    elif day is None or day == 0:
#        event_start = datetime(year, month, day=1)
#        event_end = event_start + timedelta(days=monthrange(year, month)[1])
#    else:
#        event_start = datetime(year, month, day)
#        event_end = event_start + timedelta(days=1)
#    events = (
#        db.query(Olympiad)
#        .filter(Olympiad.date_start >= event_start)
#        .filter(Olympiad.date_start < event_end)
#        .all()
#    )
#    return events
#
#
def get_event_from_database(db: Session, event: schemas.EventSchema):
    return (
        db.query(models.Event)
        .filter(
            models.Event.name == event.name, models.Event.date_start == event.date_start
        )
        .first()
    )


def create_event(db: Session, event: schemas.EventSchema):
    db_event = models.Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def delete_event(db: Session, event: schemas.EventSchema):
    db_event = get_event_from_database(db, event)
    db.delete(db_event)
    db.commit()
    return db_event


def filter_events(db: Session, filter_schema: schemas.FiltrationSchema, user_id=None):
    if user_id:
        events = get_user_events(db, user_id)
    else:
        events = db.query(models.Event)
    return (
        events.filter(
            models.Event.date_start >= filter_schema.event_date_start,
            models.Event.date_start <= filter_schema.event_date_end,
        )
        .order_by(models.Event.date_start)
        .limit(filter_schema.limit)
        .all()
    )


# def delete_event_from_database(db: Session, name: str, date: datetime):
#    event = get_event_from_database(db, name, date)
#    db.delete(event)
#    db.commit()
#    return {"data": "event deleted"}


# def create_event(db: Session, event: schemas.EventCreate):
#    if get_event_from_database_by_name_and_date(db, event.name, event.date_start):
#        raise HTTPException(detail="Event already exists", status_code=409)
#    db.add(**event.dict())
#    db.commit()
#    return {"data": "event created"}
# --------------------->User


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_events(db: Session, user_id: int):
    events = db.query(models.Event).filter(models.Event.users.any(id=user_id))
    return events


def delete_user_event(db: Session, event: schemas.EventSchema, user_id: int):
    db_event = get_event_from_database(db, event)
    events = get_user_events(db, user_id)
    events.remove(db_event)
    db.commit()
    return db_event


def add_event(db: Session, event: schemas.EventSchema, user_id: int):
    db_event = get_event_from_database(db, event)
    user = db.query(models.User).filter(models.User.id == user_id).first()
    user.events.append(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def create_user(db: Session, user: schemas.RegistrationSchema):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        **user.model_dump(exclude={"password"}), hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
