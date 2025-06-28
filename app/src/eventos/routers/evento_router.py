from fastapi import APIRouter

router = APIRouter(prefix="/eventos")


@router.get("/")
async def create_item():
    return "oie"
