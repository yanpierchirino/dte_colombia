from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_serializer

from dte_colombia.client.enums import InvoicePeriodCode

from ..components import DeliveryLine, ExtensionAmount, Item, Price, Quantity, TaxTotal


class DocumentReference(BaseModel):
    id: str
    issue_date: Optional[date] = None
    document_type_code: Optional[str] = None
    document_type: Optional[str] = None

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)


class AlternativeConditionPrice(BaseModel):
    price_amount: ExtensionAmount
    price_type_code: str
    price_type: str


class PricingReference(BaseModel):
    alternative_condition_price: AlternativeConditionPrice


class SalesInvoicePeriodLine(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    start_date: date
    description_code: InvoicePeriodCode
    description: str

    @field_serializer("start_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)


class SalesInvoiceLine(BaseModel):
    id: int
    invoiced_quantity: Quantity
    item: Item
    price: Price
    tax_totals: list[TaxTotal]
    line_extension_amount: ExtensionAmount
    invoice_period: Optional[SalesInvoicePeriodLine] = None
    free_of_charge_indicator: Optional[bool] = False
    pricing_reference: Optional[PricingReference] = None
    delivery: Optional[DeliveryLine] = None
    withholding_tax_totals: Optional[list[TaxTotal]] = None
    document_reference: Optional[list[DocumentReference]] = None
