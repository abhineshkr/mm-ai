import requests
import os
from app.model_manager.service.model_manager_generic_service import download_model_from_url
# Ensure these constants are defined properly
MODEL_BASE_PATH = os.getenv("MODEL_BASE_PATH", "D:/LLM/models/")  # Correct default value


def download_ollama_model(model_name: str, model_url: str, version: str):
    """
    Fetches the model metadata or download link from Ollama API and saves to custom path.
    
    Parameters:
    - model_name: Name of the model.
    - model_url: Ollama model download API URL.
    - version: Version of the model.
    - download_path: Custom directory where the model will be saved.
    """
    
    ollama_url = model_url
    params = {
        "version": version
    }

    response = requests.get(ollama_url, params=params)
    
    if response.status_code == 200:
        # Get download link (assuming API response returns a download URL)
        model_metadata = response.json()
        download_link = model_metadata.get('download_url')
        
        if download_link:
            return download_model_from_url(download_link, model_name, MODEL_BASE_PATH)
        else:
            raise Exception(f"No download URL found for model {model_name}.")
    else:
        raise Exception(f"Failed to fetch model {model_name}. Status: {response.status_code}")

