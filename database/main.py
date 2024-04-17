from fast_api.db import engine, Base

# from crud import (
#    create_user,
#    create_olympiad,
#    read_user_olympiad,
#    update_user_olympiad,
#    read_users_mails,
# )


# ase.metadata.drop_all(
#   bind=engine,
#   cascade="all, delete-orphan",
#   cascade="all, delete-orphan",
#
Base.metadata.create_all(bind=engine)

# create_user(username="admin", hashed_password="<PASSWORD>", email="<EMAIL>")
# create_user(username="maksim", hashed_password="123132>", email="asdsad>")
# create_user(username="leha123", hashed_password="asdasdasd", email="asdasdsd")

# print(read_users_mails("pee"))
# create_olympiad("admin", "admin", "admin")
# create_user(username="maksim", hashed_password="<PASSWORD>", email="<EMAIL>")
# create_olympiad(name="Jopasd")
# print(read_user_olympiad("maksim"))
# print(update_user_olympiad("maksim", "Jopasd"))

# for value in read_user_olympiad("maksim"):
# print(value.name)
# def create_talbes():
#    engine.echo = False
#    Base.metadata.drop_all(engine)
#    Base.metadata.create_all(engine)
#    engine.echo = False
#
#
# def insert_user():
#    with SessionLocal() as session:
#        olymp1 = Olympiad(name="Fiztech")
#        olymp2 = Olympiad(name="MMo")
#        maxim = User(
#            username="IvanIvan", hashed_password="Tt228", olympiads=[olymp1, olymp2]
#        )
#        denis = User(username="Max112", hashed_password="qasdf", olympiads=[])
#        session.add_all([maxim, denis, olymp1, olymp2])
#        session.commit()
#
#
# create_talbes()
# insert_user()
