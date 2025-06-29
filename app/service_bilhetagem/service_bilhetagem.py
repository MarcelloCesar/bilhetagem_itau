from fastapi import FastAPI
from src.routers import evento_router

app = FastAPI()
app.include_router(evento_router.router)
