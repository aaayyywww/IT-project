from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import List

from database import crud
from dependencies import (
    get_db,
    get_current_active_user,
)
import schemas

user_router = APIRouter(prefix="/users")


@user_router.post("/register", tags=["auth"], response_model=schemas.UserSchema)
async def create_user(user: schemas.RegistrationSchema, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(
            detail="Email already registered", status_code=status.HTTP_400_BAD_REQUEST
        )
    return crud.create_user(db, user)


@user_router.post(
    "/get_events", tags=["event"], response_model=List[schemas.EventSchema]
)
async def get_events(
    current_user: schemas.UserSchema = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    return crud.get_user_events(db, current_user.id)


@user_router.post("/add_event", tags=["event"], response_model=schemas.EventSchema)
async def add_event(
    event: schemas.EventSchema,
    db: Session = Depends(get_db),
    current_user: schemas.UserSchema = Depends(get_current_active_user),
):
    if not crud.get_event_from_database(db, event):
        raise HTTPException(
            detail="Event not found", status_code=status.HTTP_404_NOT_FOUND
        )
    if crud.get_event_from_database(db, event) in crud.get_user_events(
        db, current_user.id
    ):
        raise HTTPException(
            detail="Event already registered", status_code=status.HTTP_400_BAD_REQUEST
        )
    return crud.add_event(db, event, current_user.id)


@user_router.delete("/delete_event", tags=["event"], response_model=schemas.EventSchema)
async def delete_event(
    event: schemas.EventSchema,
    db: Session = Depends(get_db),
    current_user: schemas.UserSchema = Depends(get_current_active_user),
):
    if crud.get_event_from_database(db, event) not in crud.get_user_events(
        db, current_user.id
    ):
        raise HTTPException(
            detail="Event not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return crud.delete_user_event(db, event, current_user.id)


@user_router.post(
    "/filter_events", tags=["event"], response_model=List[schemas.EventSchema]
)
async def filter_user_events(
    filter_schema: schemas.FiltrationSchema,
    db: Session = Depends(get_db),
):
    return crud.filter_events(db, filter_schema)


@user_router.post(
    "/filter_user_events", tags=["event"], response_model=List[schemas.EventSchema]
)
async def filter_user_events(
    filter_schema: schemas.FiltrationSchema,
    db: Session = Depends(get_db),
    current_user: schemas.UserSchema = Depends(get_current_active_user),
):
    return crud.filter_events(db, filter_schema, current_user.id)
