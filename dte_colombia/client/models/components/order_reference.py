from datetime import date

from pydantic import BaseModel, field_serializer


class OrderReference(BaseModel):
    id: str
    issue_date: date

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
