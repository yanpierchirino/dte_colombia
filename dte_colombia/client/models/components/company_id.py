from pydantic import BaseModel, ConfigDict

from dte_colombia.client.enums import TaxIdentifierType


class CompanyID(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    agency_id: str = "195"
    agency_name: str = "CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)"
    verification_digit: str
    identification_type: TaxIdentifierType
    identification: str
