from pydantic import BaseModel, ConfigDict

from dte_colombia.client.enums import Taxes


class TaxScheme(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Taxes
    name: str


class TaxCategory(BaseModel):
    percent: float
    tax_scheme: TaxScheme


class TaxLevelCode(BaseModel):
    name: str
    code: str
