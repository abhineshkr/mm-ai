import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load configurable parameters from environment variables with defaults
DEFAULT_MODEL_URL = os.getenv("MODEL_URL", "https://huggingface.co/Orenguteng/Llama-3.1-8B-Lexi-Uncensored-GGUF/resolve/main/Llama-3.1-8B-Lexi-Uncensored_Q5_fixedrope.gguf")
DEFAULT_MODELS_DIR = os.getenv("MODELS_DIR", "models")
LOCK_TIMEOUT = int(os.getenv("LOCK_TIMEOUT", "1200"))  # in seconds
MIN_FILE_SIZE_MB = float(os.getenv("MIN_FILE_SIZE_MB", "100"))  # minimum file size in MB
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DEFAULT_MODEL_NAME=os.getenv("DEFAULT_MODEL_NAME")
PDF_PROCESS_IMAGE_PATH =os.getenv("PDF_PROCESS_IMAGE_PATH","D:/LLM/pdfs/images")
