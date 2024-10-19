from datetime import date

from pydantic import BaseModel, field_serializer
from pydantic.dataclasses import dataclass

from .uuid import UUID


class BillingDocumentReference(BaseModel):
    id: str
    uuid: UUID
    issue_date: date

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)


class BillingReference(BaseModel):
    document_reference: BillingDocumentReference


@dataclass
class InvoiceDocumentReferenceData:
    id: str
    uuid: str
    issue_date: date

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)


@dataclass
class BillingReferenceData:
    document_reference: InvoiceDocumentReferenceData
