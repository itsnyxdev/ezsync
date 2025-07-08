import os

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import mongodb_connect, mongodb_disconnect


@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongodb_connect()
    yield
    await mongodb_disconnect()


app = FastAPI()

@app.get("/")
async def root():
    return "Hello World!"