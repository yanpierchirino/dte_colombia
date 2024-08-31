from pydantic import BaseModel


class Response(BaseModel):
    success: bool
    message: str
    data: dict
