from datetime import date

from pydantic import BaseModel, field_serializer


class InvoiceResolution(BaseModel):
    prefix: str
    resolution_date: date
    from_number: int
    to_number: int
    valid_date_from: date
    valid_date_to: date
    technical_key: str

    @field_serializer(
        "resolution_date", "valid_date_from", "valid_date_to", when_used="always"
    )
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
