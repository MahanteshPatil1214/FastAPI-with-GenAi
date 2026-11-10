from fastapi import FastAPI
from src.routes.productRoute import productRoute

app=FastAPI(title="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")

@app.get("/home")
def home():
    return {
        "message" : "Welcome to my FastAPI application!"
    }

### CRUD APIs Endpoints - JSON file

app.include_router(productRoute,prefix="/products")