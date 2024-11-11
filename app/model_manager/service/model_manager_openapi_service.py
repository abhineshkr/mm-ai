# services/openapi_downloader.py
import os
import requests

# Ensure these constants are defined properly
MODEL_BASE_PATH = os.getenv("MODEL_BASE_PATH", "D:/LLM/models/")  # Correct default value

def download_openapi_model(api_url: str, model_name: str):
    
    # Use os.path.join for correct cross-platform paths
    model_dir = os.path.join(MODEL_BASE_PATH, model_name)
    filename = os.path.join(model_dir, model_name)  # Ensure file is saved in the right directory
    
    print("File Name:", filename)
    print("Model Directory:", model_dir)
    
    # Normalize paths
    model_dir = os.path.normpath(model_dir)
    filename = os.path.normpath(filename)
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

     # Save model and tokenizer
    if not os.path.exists(filename):    
        # Example request to download model
        response = requests.get(api_url)

        if response.status_code == 200:
            with open(os.path.join(model_dir, "model.bin"), 'wb') as f:
                f.write(response.content)
            return f"Model downloaded from {api_url} to {model_dir}"
        else:
            return f"Failed to download model from {api_url}"
