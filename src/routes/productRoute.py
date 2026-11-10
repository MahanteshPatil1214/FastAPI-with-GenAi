from fastapi import APIRouter
from src.utils.utils import getAllProducts

productRoute = APIRouter()

@productRoute.get("/")
def getALLProducts():
    return getAllProducts()
