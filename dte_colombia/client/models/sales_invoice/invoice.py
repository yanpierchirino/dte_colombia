from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_serializer

from dte_colombia.client.enums import InvoiceCustomizationID, InvoiceTypeCode

from ..components import (
    AccountingParty,
    Delivery,
    DeliveryTerms,
    DocumentPeriod,
    InvoiceControl,
    InvoiceDocumentReference,
    LegalMonetaryTotal,
    OrderReference,
    PaymentExchangeRate,
    PaymentMeans,
    PrepaidPayment,
    TaxTotal,
)
from .invoice_line import SalesInvoiceLine


class SalesInvoiceData(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: str
    customization_id: InvoiceCustomizationID
    invoice_type_code: InvoiceTypeCode
    currency_code: str
    issue_date: date
    issue_time: str
    due_date: date
    invoice_control: InvoiceControl
    supplier_party: AccountingParty
    customer_party: AccountingParty
    tax_totals: list[TaxTotal]
    payment_means: PaymentMeans
    lines: list[SalesInvoiceLine]
    legal_monetary_total: LegalMonetaryTotal
    payment_exchange_rate: Optional[PaymentExchangeRate] = None
    invoice_period: Optional[DocumentPeriod] = None
    order_reference: Optional[OrderReference] = None
    prepaid_payment: Optional[PrepaidPayment] = None
    withholding_tax_totals: Optional[list[TaxTotal]] = None
    billing_reference: Optional[list[InvoiceDocumentReference]] = None
    delivery_terms: Optional[DeliveryTerms] = None
    delivery: Optional[Delivery] = None
    note: str = ""

    @field_serializer("issue_date", "due_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
