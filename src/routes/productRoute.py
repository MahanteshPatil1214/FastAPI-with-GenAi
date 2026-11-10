from fastapi import APIRouter, HTTPException
from src.utils.utils import getAllProducts

productRoute = APIRouter()

@productRoute.get("/")
def getALLProducts(id:int=None):
    allProducts = getAllProducts()
    if not id :
       return allProducts

    
    for product in allProducts:
            if product["id"] == id:
                return product
    return HTTPException(status_code=404, detail=f"Product not found for {id}")
    
    

@productRoute.get("/{id}")
def getProductById(id:int):
    allProducts = getAllProducts()
    for product in allProducts:
        if product["id"] == id:
            return product
    return HTTPException(status_code=404, detail=f"Product not found for {id}")
