from sqlalchemy import create_engine
from config import settings
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from typing import Annotated

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)


session_factory = sessionmaker(sync_engine)
intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    pass


class OlympiadaOrm(Base):
    __tablename__ = "olymps"
    
    id: Mapped[intpk]
    name: Mapped[str]
    date: Mapped[str]
    time: Mapped[str]
    tour: Mapped[str]
    subject: Mapped[str]
    level: Mapped[str]
    link: Mapped[str]
    university: Mapped[str]
