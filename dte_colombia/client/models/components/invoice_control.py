from datetime import date

from pydantic import BaseModel, field_serializer


class AuthorizationPeriod(BaseModel):
    start_date: date
    end_date: date

    @field_serializer("start_date", "end_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)


class AuthorizedInvoices(BaseModel):
    prefix: str
    range_from: int
    range_to: int


class InvoiceControl(BaseModel):
    invoice_authorization: int
    authorization_period: AuthorizationPeriod
    authorized_invoices: AuthorizedInvoices
