from datetime import date

from pydantic import BaseModel, field_serializer


class DocumentPeriod(BaseModel):
    start_date: date
    start_time: str
    end_date: date
    end_time: str

    @field_serializer("start_date", "end_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
