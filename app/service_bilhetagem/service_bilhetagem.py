from fastapi import FastAPI
from src.routers import evento_router
from src.routers import reserva_router


app = FastAPI()
app.include_router(evento_router.router)
app.include_router(reserva_router.router)
