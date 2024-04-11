from database import Base, OlympiadaOrm, sync_engine, session_factory
from parsing_olympiads_postupashki import Parser


def create_talbes():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    data = Parser.get_year_olympiads()

    with session_factory() as session:
        for elem in data:
            olympiada = OlympiadaOrm(name=elem["name"],
                                     date=elem["date"],
                                     time=elem["time"],
                                     tour=elem["tour"],
                                     subject=elem["subject"],
                                     level=elem["level"],
                                     link=elem["link"],
                                     university=elem["university"]
                                     )
            session.add(olympiada)
            session.commit()
