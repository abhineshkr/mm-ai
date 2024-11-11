import os
import urllib.request

from app.utils.logger.logger_manager import logger



def create_directory(directory_path: str):
    """
    Ensures the given directory exists. Creates it if not.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        logger.info(f"Created directory: {directory_path}")
    else:
        logger.info(f"Directory already exists: {directory_path}")