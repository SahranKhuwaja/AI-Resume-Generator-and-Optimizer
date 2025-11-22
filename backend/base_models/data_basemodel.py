from pydantic import BaseModel
from typing import Optional

class Data(BaseModel):
    text: str
    success: bool
    error: Optional[str] = None