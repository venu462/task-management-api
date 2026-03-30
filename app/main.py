#MAIN WORKFLOW
from fastapi import FastAPI
from app.api.router import api_router
from app.models import *

app = FastAPI(
    title="Task Manager API",
)

app.include_router(api_router)

@app.get("/health")
def health_check():
    return{"status": "ok"}

