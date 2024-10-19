from pydantic import BaseModel

from .extension_amount import ExtensionAmount
from .quantity import Quantity


class Price(BaseModel):
    price_amount: ExtensionAmount
    base_quantity: Quantity
