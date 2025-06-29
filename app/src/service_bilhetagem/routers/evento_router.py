from fastapi import APIRouter
from src.service_bilhetagem.controllers.http.eventos_http_controller import (
    http_get_dados_evento, http_get_lista_eventos
)

router = APIRouter(prefix="/eventos")


@router.get("/")
async def rota_get_lista_eventos():
    return http_get_lista_eventos()


@router.get("/{id_evento}")
async def rota_get_evento(id_evento: str):
    return http_get_dados_evento(id_evento)
