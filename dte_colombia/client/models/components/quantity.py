from pydantic import BaseModel


class Quantity(BaseModel):
    unit_code: str
    quantity: float
