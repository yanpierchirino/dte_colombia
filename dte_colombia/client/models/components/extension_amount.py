from pydantic import BaseModel


class ExtensionAmount(BaseModel):
    currency_id: str
    amount: float
