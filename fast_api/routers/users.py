from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from fast_api.dependencies import (
    get_db,
    check_permission_teacher,
    check_permission_admin,
    check_permission_developer,
)
from database import User, Roles
from fast_api.schemas import CreateUser
from .auth import pwd_context

user_router = APIRouter(prefix="/users")


@user_router.post("/register", tags=["Users"])
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    if user.role in (Roles.admin, Roles.developer):
        raise HTTPException(
            detail="You are not allowed to create a user with this role.",
            status_code=status.HTTP_403_FORBIDDEN,
        )
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
    )
    if (db_user.email,) in db.query(User.email).all():
        raise HTTPException(
            detail="Email already registered", status_code=status.HTTP_400_BAD_REQUEST
        )
    else:
        db.add(db_user)
        db.commit()
    return {"message": "User created"}


@user_router.post("/check_permission_teacher", tags=["Users"])
async def check_teacher(user: User = Depends(check_permission_teacher)):
    print(user.role)
    return user.role


@user_router.post("/check_permission_admin", tags=["Users"])
async def check_admin(user: User = Depends(check_permission_admin)):
    print(user.role)
    return user.role


@user_router.post("/check_permission_developer", tags=["Users"])
async def check_teacher(user: User = Depends(check_permission_developer)):
    print(user.role)
    return user.role
