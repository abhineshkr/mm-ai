# services/huggingface_downloader.py
import os
from transformers import AutoModel, AutoTokenizer

# Ensure these constants are defined properly
MODEL_BASE_PATH = os.getenv("MODEL_BASE_PATH", "D:/LLM/models/")  # Correct default value

def download_huggingface_model(model_name: str):    
    # Use os.path.join for correct cross-platform paths
    model_dir = os.path.join(MODEL_BASE_PATH, model_name)
    filename = os.path.join(model_dir, model_name)  # Ensure file is saved in the right directory
    
    print("File Name:", filename)
    print("Model Directory:", model_dir)
    
    # Normalize paths
    model_dir = os.path.normpath(model_dir)
    filename = os.path.normpath(filename)
    
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)  # Ensure the directory is created

    # Downloading the model and tokenizer
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Save model and tokenizer
    if not os.path.exists(filename):
        model.save_pretrained(model_dir)
        tokenizer.save_pretrained(model_dir)
        
        
    return f"Model {model_name} downloaded and saved to {model_dir}"
