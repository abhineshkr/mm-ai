# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddlewarex

from app.utils.logger.logger_manager import logger
from app.model_manager.router.model_manager_generic_router import model_manager_generic_router
from app.model_manager.router.model_manager_huggingface_router import model_manager_huggingface_router
from app.model_manager.router.model_manager_ollama_router import model_manager_ollama_router
from app.model_manager.router.model_manager_openapi_router import model_manager_openapi_router



# Initialize FastAPI app
app = FastAPI()
app.include_router(model_manager_generic_router,tags=["Generic Model Manager"])
app.include_router(model_manager_huggingface_router,tags=["HuggingFace Model Manager"])
app.include_router(model_manager_ollama_router,tags=["OpenAPI Model Manager"])
app.include_router(model_manager_openapi_router,tags=["Ollama Model Manager"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)