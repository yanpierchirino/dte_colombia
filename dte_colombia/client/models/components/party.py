from typing import Optional

from pydantic import BaseModel, ConfigDict

from dte_colombia.client.enums import OrganizationType

from .company_id import CompanyID
from .contact import Contact
from .physical_location import PhysicalLocation
from .tax import TaxLevelCode, TaxScheme


class PartyName(BaseModel):
    name: str


class CorporateRegistrationScheme(BaseModel):
    id: str
    name: str = "0000000"


class PartyTaxScheme(BaseModel):
    registration_name: str
    company_id: CompanyID
    tax_level_code: TaxLevelCode
    tax_scheme: TaxScheme


class PartyLegalEntity(BaseModel):
    registration_name: str
    company_id: CompanyID
    corporate_registration_scheme: Optional[CorporateRegistrationScheme] = None


class Party(BaseModel):
    party_name: list[PartyName]
    physical_location: PhysicalLocation
    party_tax_scheme: PartyTaxScheme
    party_legal_entity: Optional[PartyLegalEntity] = None
    contact: Contact


class AccountingParty(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    organization_type: OrganizationType
    party: Party
