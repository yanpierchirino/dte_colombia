from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_serializer

from dte_colombia.client.enums import CreditNoteCustomizationID, CreditNoteTypeCode

from ..components import (
    AccountingParty,
    BillingReferenceData,
    CreditNoteDiscrepancyResponse,
    Delivery,
    DeliveryTerms,
    DocumentPeriod,
    LegalMonetaryTotal,
    PaymentMeans,
    TaxTotal,
)
from .credit_note_line import CreditNoteLine


class CreditNoteData(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: str
    customization_id: CreditNoteCustomizationID
    currency_code: str
    issue_date: date
    issue_time: str
    credit_note_type_code: CreditNoteTypeCode
    discrepancy_response: CreditNoteDiscrepancyResponse
    supplier_party: AccountingParty
    customer_party: AccountingParty
    tax_totals: list[TaxTotal]
    lines: list[CreditNoteLine]
    legal_monetary_total: LegalMonetaryTotal
    payment_means: PaymentMeans
    invoice_period: Optional[DocumentPeriod] = None
    billing_reference: Optional[list[BillingReferenceData]] = None
    delivery: Optional[Delivery] = None
    delivery_terms: Optional[DeliveryTerms] = None
    note: str = ""

    @field_serializer("issue_date", when_used="always")
    def serialize_date(self, value: date) -> str:
        try:
            return value.isoformat()
        except AttributeError:
            return str(value)
