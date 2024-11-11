# file: api/huggingface_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model_manager.schema.huggingface_model_download_request import HuggingFaceDownloadModelRequest
from app.model_manager.service.model_manager_huggingface_service import download_huggingface_model

# Define a router object
model_manager_huggingface_router = APIRouter()



# Define the endpoint that will trigger the model download
@model_manager_huggingface_router.post("/download/model/huggingface")
async def download_model(request: HuggingFaceDownloadModelRequest):
    try:
        result = download_huggingface_model(request.model_name)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

