from database.models import User, Olympiad
from fast_api.db import SessionLocal


def create_user(
    username: str,
    email: str,
    hashed_password: str,
    role: str = None,  # ask
):
    with SessionLocal() as session:
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            role=role,
            olympiads=[],
        )
        session.add(user)
        session.commit()


def create_olympiad(
    name: str,
):
    with SessionLocal() as session:
        olympiad = Olympiad(name=name)
        session.add(olympiad)
        session.commit()


def read_user_olympiad(name: str):
    with SessionLocal() as session:
        user = session.query(User).filter_by(username=name).first()
        if user:
            return user.olympiads


def read_users_mails(email: str):
    with SessionLocal() as session:
        return [user.email for user in session.query(User)]


def update_user_olympiad(username: str, olympiad_name: str):
    with SessionLocal() as session:
        user = session.query(User).filter_by(username=username).first()
        olympiad = session.query(Olympiad).filter_by(name=olympiad_name).first()
        if user and olympiad:
            user.olympiads.append(olympiad)
            session.commit()
        return user.olympiads
