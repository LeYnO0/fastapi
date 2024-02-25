from fastapi import FastAPI
from routers.routers import router as tasks_router

app = FastAPI()

app.include_router(
    router=tasks_router,
    prefix='/tasks'
)
