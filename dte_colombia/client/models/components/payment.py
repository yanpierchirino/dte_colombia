from datetime import date

from pydantic import BaseModel, field_serializer

from .extension_amount import ExtensionAmount


class PaymentMeans(BaseModel):
    id: str
    code: str
    due_date: date
    payment_id: str

    @field_serializer("due_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)


class PrepaidPayment(BaseModel):
    id: str
    paid_amount: ExtensionAmount
    received_date: date
    paid_date: date
    instruction: str

    @field_serializer("received_date", "paid_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
