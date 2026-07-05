from contextlib import asynccontextmanager
from fastapi import FastAPI
from controller import router, init_producer, stop_producer

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_producer()
    yield
    await stop_producer()

app = FastAPI(lifespan=lifespan)
app.include_router(router)