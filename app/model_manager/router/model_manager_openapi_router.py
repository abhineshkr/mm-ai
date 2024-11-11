# file: api/openapi_model_manager_openapi_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model_manager.schema.openapi_model_download_request import openApiaModelDownloadRequest
from app.model_manager.service.model_manager_openapi_service import download_openapi_model


# Define a model_manager_openapi_router object
model_manager_openapi_router = APIRouter()



# Define the endpoint to download the model from an OpenAPI URL
@model_manager_openapi_router.post("/download/model/openapi")
async def download_model(request: openApiaModelDownloadRequest):
    try:
        result = download_openapi_model(
            api_url=request.api_url,
            model_name=request.model_name
        )
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

