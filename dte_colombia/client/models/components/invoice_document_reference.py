from datetime import date

from pydantic import BaseModel, field_serializer
from .uuid import DocumentUUID


class InvoiceDocumentReference(BaseModel):
    id: str
    uuid: DocumentUUID
    issue_date: date
    document_description: str

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
