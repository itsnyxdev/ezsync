import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request, status
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from starlette.responses import JSONResponse

from app.api.v1.auth import router as auth_router
from app.config.settings import CsrfSettings
from app.models import Base
from app.utils.database import close_mariadb, init_mariadb, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(title="EzSync API", debug=True, lifespan=lifespan)

app.include_router(router=auth_router, prefix="/api")

@CsrfProtect.load_config
def get_csrf_config() -> CsrfSettings:
    csrf_settings = CsrfSettings()
    return csrf_settings

@app.get("/1i7qaaLths3y", response_class=JSONResponse)
async def get_csrf(request: Request, csrf_protect: CsrfProtect = Depends()):
    csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
    response = JSONResponse(
        content= {
            "token": csrf_token
        },
        status_code=status.HTTP_200_OK
    )

    csrf_protect.set_csrf_cookie(signed_token, response)
    return response


@app.get("/")
def root():
    return {"message": "EzSync API :)"}

@app.exception_handler(CsrfProtectError)
async def csrf_protect_exception_handler(_: Request, exc: CsrfProtectError):
  return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

