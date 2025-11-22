from pydantic import BaseModel
from typing import Optional

class Response(BaseModel):
    filename: Optional[str] = None
    content_type: Optional[str] = None
    success: bool
    generated_resume: Optional[str] = None
    error: Optional[str] = None