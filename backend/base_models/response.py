from pydantic import BaseModel

class Response(BaseModel):
    generated_resume: str