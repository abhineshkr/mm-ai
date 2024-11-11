import os
from fastapi import Query,APIRouter
from app.utils.logger.logger_manager import logger
from app.config.config import DEFAULT_MODEL_URL, DEFAULT_MODELS_DIR, LOCK_TIMEOUT, MIN_FILE_SIZE_MB,DEFAULT_MODEL_NAME
from app.model_manager.schema.model_download_response_schema import DownloadResponse
from app.model_manager.service.model_manager_generic_service import download_model_from_url



model_manager_generic_router = APIRouter()


@model_manager_generic_router.post("/download/model")
async def download_models(
    model_url: str = Query(default=DEFAULT_MODEL_URL),
    models_name: str = Query(default=DEFAULT_MODEL_NAME)
    
) -> DownloadResponse:
    """
    Downloads model from the specified URL and saves it in the given directory.
    Uses a lock file to ensure no other download process is running concurrently.
    """
    download_status = []

    

    # Download the model and get the status
    status = download_model_from_url(model_url,models_name)

    # Append the status of the download
    download_status.append(status)
    
    return DownloadResponse(model_name=[os.path.basename(model_url)], status=download_status)
