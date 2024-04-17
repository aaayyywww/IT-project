from database import SessionLocal, User, Roles
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from routers.auth import get_current_active_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_permission_teacher(user: User = Depends(get_current_active_user)):
    if user.role != Roles.student:
        return user
    else:
        raise HTTPException(detail="Permission Denied", status_code=403)


def check_permission_admin(user: User = Depends(check_permission_teacher)):
    if user.role != Roles.teacher:
        return user
    else:
        raise HTTPException(detail="Permission Denied", status_code=403)


def check_permission_developer(user: User = Depends(check_permission_admin)):
    if user.role != Roles.admin:
        return user
    else:
        raise HTTPException(detail="Permission Denied", status_code=403)
