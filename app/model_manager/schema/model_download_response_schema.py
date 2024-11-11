from pydantic import BaseModel
from typing import List, Dict

class DownloadResponse(BaseModel):
    model_name: List[str]
    status: List[Dict[str, str]]