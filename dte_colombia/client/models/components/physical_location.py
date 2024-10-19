from pydantic import BaseModel

from .address import Address


class PhysicalLocation(BaseModel):
    address: Address
