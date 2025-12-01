from pydantic import BaseModel
from typing import Optional

class Response(BaseModel):
    pdf_stream: Optional[bytes] = None,
    as_attachment: Optional[bool] = None,
    download_name: Optional[str] = None,
    mimetype: Optional[str] = None
    success: bool
    error: Optional[str] = None