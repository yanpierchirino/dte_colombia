from pydantic import BaseModel

from .address import Address
from .contact import Contact
from .party import PartyLegalEntity, PartyName, PartyTaxScheme


class DeliveryLocationId(BaseModel):
    id: str
    name: str
    code: str


class DeliveryLocation(BaseModel):
    id: DeliveryLocationId


class DeliveryLine(BaseModel):
    delivery_location: DeliveryLocation


class DeliveryPhysicalLocation(BaseModel):
    address: Address


class DeliveryParty(BaseModel):
    party_name: PartyName
    physical_location: DeliveryPhysicalLocation
    party_tax_scheme: PartyTaxScheme
    party_legal_entity: PartyLegalEntity
    contact: Contact


class Delivery(BaseModel):
    delivery_address: Address
    delivery_party: DeliveryParty


class DeliveryTerms(BaseModel):
    special_terms: str
    loss_risk_responsibility_code: str
    loss_risk: str
