from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.auth import router as auth_router
from app.api.v1.jobs import router as jobs_router
from app.models import Base
from app.utils.database import engine, init_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongodb()
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(title="EzSync API", debug=True, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router=auth_router, prefix="/api")
app.include_router(router=jobs_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "EzSync API :)"}
