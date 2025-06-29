from fastapi import APIRouter

router = APIRouter(prefix="/eventos")


@router.get("/")
async def rota_get_eventos():
    return "oie"
