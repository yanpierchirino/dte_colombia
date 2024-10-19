from datetime import date

from pydantic import BaseModel, field_serializer


class InvoiceDocumentUUID(BaseModel):
    code: str
    name: str


class InvoiceDocumentReference(BaseModel):
    id: str
    uuid: InvoiceDocumentUUID
    issue_date: date
    document_description: str

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
