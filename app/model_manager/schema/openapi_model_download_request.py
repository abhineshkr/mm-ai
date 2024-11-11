
from pydantic import BaseModel


# Define a Pydantic model to validate the input
class openApiaModelDownloadRequest(BaseModel):
    api_url: str
    model_name: str