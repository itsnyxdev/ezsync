import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.utils.database import close_mariadb, init_mariadb



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_mdb, = await asyncio.gather(init_mariadb())
    app.state.mariadb = init_mdb
    yield
    await asyncio.gather(close_mariadb(app.state.mariadb))

app = FastAPI(title="EzSync API", debug=True, lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "EzSync API :)"}