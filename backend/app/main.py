import os

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.routes.auth import router
from app.config.database import create_all_tables, mongodb_connect, mongodb_disconnect

create_all_tables()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongodb_connect()
    yield
    await mongodb_disconnect()


app = FastAPI(debug=True)

app.include_router(router=router)

@app.get("/")
async def root():
    return "Hello World!"