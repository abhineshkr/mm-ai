
from pydantic import BaseModel


# Define a Pydantic model to validate the input
class ollamaModelDownloadRequest(BaseModel):
    model_name: str
    model_url: str
    version: str