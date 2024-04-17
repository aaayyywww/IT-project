from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from database.db import SessionLocal
from fast_api.dependencies import get_db
from database import Olympiad, User
from fast_api.schemas import CreateOlympiad
from .auth import get_current_active_user

# from typing import Annotated

olympiad_router = APIRouter(prefix="/olympiads")


@olympiad_router.post("/create", tags=["Olimpiads"])
async def create_olympiad(
    olympiad: CreateOlympiad,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    olympiad = Olympiad(**olympiad.dict())
    db.add(olympiad)
    db.commit()
    return {"message": "Olimpiad created"}
