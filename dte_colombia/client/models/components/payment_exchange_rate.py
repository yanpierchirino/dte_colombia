from datetime import date

from pydantic import BaseModel, field_serializer


class PaymentExchangeRate(BaseModel):
    source_currency_code: str
    source_currency_base_rate: float
    target_currency_code: str
    target_currency_base_rate: float
    calculation_rate: float
    issue_date: date

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
