from pydantic import BaseModel


class CountryName(BaseModel):
    language_id: str = "es"
    name: str


class Country(BaseModel):
    code: str
    name: CountryName
