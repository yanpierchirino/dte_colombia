from pydantic import BaseModel


class ItemIdentification(BaseModel):
    id: str


class StandardItemIdentificationId(BaseModel):
    id: str
    agency_id: str
    name: str
    code: str


class StandardItemIdentification(BaseModel):
    id: StandardItemIdentificationId


class Item(BaseModel):
    description: str
    sellers_item_identification: ItemIdentification
    standard_item_identification: StandardItemIdentification
