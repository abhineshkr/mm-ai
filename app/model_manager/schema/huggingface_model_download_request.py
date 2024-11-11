
from pydantic import BaseModel


# Define a Pydantic model to validate the input
class HuggingFaceDownloadModelRequest(BaseModel):
    model_name: str