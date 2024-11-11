# file: api/ollama_router.py

from fastapi import APIRouter, HTTPException
from app.model_manager.schema.ollama_model_download_request import ollamaModelDownloadRequest
from app.model_manager.service.model_manager_ollama_service import download_ollama_model


# Define a router object
model_manager_ollama_router = APIRouter()



# Endpoint to fetch and download the model from Ollama
@model_manager_ollama_router.post("/download/model/ollama")
async def fetch_model(request: ollamaModelDownloadRequest):
    try:
        result = download_ollama_model(
            model_name=request.model_name,
            model_url=request.model_url,
            version=request.version
        )
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

