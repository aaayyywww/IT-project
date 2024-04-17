from sqlalchemy import create_engine
from database.config import settings
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
    pool_size=20,
    max_overflow=5,
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


class Base(DeclarativeBase):
    pass
