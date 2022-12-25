from fastapi import APIRouter
from app.routers.generate.service import get_prediction_data
from fastapi.responses import JSONResponse

generate = APIRouter(
    prefix="/generate",
    tags=["predict"],
    responses={404: {"description": "Not found"}},
)


@generate.get("/")
async def generate_():
    data = await get_prediction_data()
    return data
