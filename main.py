import uvicorn
from fastapi import FastAPI

from routers import user_router, admin_router, auth_router
from database import (
    engine,
    SessionLocal,
    Base,
)  # сделать файл конфиг для дб с контекстным менеджером!!!!!!!

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(admin_router)
app.include_router(user_router)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
