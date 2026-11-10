from fastapi import FastAPI

app=FastAPI(title="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")

@app.get("/")
def home():
    return {
        "message" : "Welcome to my FastAPI application!"
    }