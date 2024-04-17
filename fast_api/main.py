import uvicorn
from fastapi import FastAPI

from routers.olimpiads import olympiad_router
from routers.users import user_router
from routers.auth import auth_router
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(olympiad_router)
app.include_router(user_router)
app.include_router(auth_router)

# @app.get("/")
# async def root():
#   return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#   return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
