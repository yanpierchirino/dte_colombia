from pydantic import BaseModel

from .country import Country


class AddressLine(BaseModel):
    line: str


class Address(BaseModel):
    id: str
    city_name: str
    country_subentity: str
    country_subentity_code: str
    address_lines: list[AddressLine]
    country: Country
