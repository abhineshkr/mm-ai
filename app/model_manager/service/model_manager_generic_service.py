import os
import urllib.request
from filelock import FileLock, Timeout
from app.utils.logger.logger_manager import logger
from app.utils.director_manager import create_directory


# Ensure these constants are defined properly
MODEL_BASE_PATH = os.getenv("MODEL_BASE_PATH", "D:/LLM/models/")  # Correct default value
LOCK_TIMEOUT = int(os.getenv("LOCK_TIMEOUT", 60))
MIN_FILE_SIZE_MB = float(os.getenv("MIN_FILE_SIZE_MB", 1))

def download_model_from_url(model_url: str, model_name: str) -> dict:
    """
    Downloads the model from the specified URL, saves it in the provided directory,
    and checks if the download was successful by validating the file size.
    """
    
    # Split to get name without extension
    model_name_without_extension = model_name.rsplit('.', 1)[0]
    
    # Use os.path.join for correct cross-platform paths
    model_dir = os.path.join(MODEL_BASE_PATH, model_name_without_extension)
    filename = os.path.join(model_dir, model_name)  # Ensure file is saved in the right directory
    
    print("File Name:", filename)
    print("Model Directory:", model_dir)
    
    # Normalize paths
    model_dir = os.path.normpath(model_dir)
    filename = os.path.normpath(filename)
    
    logger.info(f"Model Directory: {model_dir}")
    logger.info(f"File Name: {filename}")
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)  # Ensure the directory is created
    
    status = {"url": model_url, "status": "success", "message": "File already exists."}
    
    lock = FileLock(os.path.join(model_dir, "download.lock"))
    
    try:
        with lock.acquire(timeout=LOCK_TIMEOUT):
            if not os.path.exists(filename):
                logger.info(f"Downloading model: {model_name} from {model_url}...")
                urllib.request.urlretrieve(model_url, filename)
                
                # Validate file size
                file_size = os.path.getsize(filename) / (1024 * 1024)
                if file_size < MIN_FILE_SIZE_MB:
                    os.remove(filename)
                    status["status"] = "failure"
                    status["message"] = f"Downloaded file is too small ({file_size:.2f} MB), possibly invalid."
                    logger.error(status["message"])
                else:
                    logger.info(f"Successfully downloaded: {filename} (Size: {file_size:.2f} MB)")
                    status["message"] = f"Successfully downloaded {model_name}."
            else:
                logger.info(f"Model file already exists: {filename}")
    except Timeout:
        logger.error(f"Error: Could not acquire lock for downloading {model_name}")
        status["status"] = "failure"
        status["message"] = "Could not acquire lock for downloading."
    
    return status
