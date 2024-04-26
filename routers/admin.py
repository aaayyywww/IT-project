from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status

from database import crud

import dependencies
import schemas


admin_router = APIRouter(
    prefix="/admin", dependencies=[Depends(dependencies.check_permission_admin)]
)


@admin_router.post("/create_event", tags=["admin"], response_model=schemas.EventSchema)
async def create_event(
    event: schemas.EventSchema, db: Session = Depends(dependencies.get_db)
):
    if crud.get_event_from_database(db, event):
        raise HTTPException(
            detail="Event already exists", status_code=status.HTTP_400_BAD_REQUEST
        )
    return crud.create_event(db=db, event=event)


@admin_router.delete(
    "/delete_event", tags=["admin"], response_model=schemas.EventSchema
)
async def delete_event(
    event: schemas.EventSchema, db: Session = Depends(dependencies.get_db)
):
    if not crud.get_event_from_database(db, event):
        raise HTTPException(
            detail="Event does not exist", status_code=status.HTTP_400_BAD_REQUEST
        )
    return crud.delete_event(db=db, event=event)
