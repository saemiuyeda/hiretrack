from fastapi import FastAPI
from .routers.applications import router as application

app = FastAPI()

app.include_router(application)

@app.get("/")
def health_check():
    return {
        "status": "healthy"
    }