from fastapi import APIRouter, Request, HTTPException
from src.controllers.http.reservas_http_controller import (
    http_post_criar_reserva
)
from src.domain.exceptions.request_validation_exception import \
    RequestValidationException
from src.util.app_logger import AppLogger

router = APIRouter(prefix="/reservas")
logger = AppLogger().get_logger()


@router.post("/")
async def rota_post_criar_reserva(request: Request):
    headers = dict(request.headers)
    try:
        body = await request.json()
    except Exception:
        body = {}

    try:
        return http_post_criar_reserva(headers, body)
    except RequestValidationException as e:
        raise HTTPException(status_code=422, detail=e.errors)
    except Exception as e:
        logger.exception(e)
        return {"error": "Erro desconhecido"}
