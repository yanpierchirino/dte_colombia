from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict

from dte_colombia.client.enums import DebitNoteCustomizationID

from ..components import (
    AccountingParty,
    BillingReferenceData,
    CreditNoteDiscrepancyResponse,
    Delivery,
    DeliveryTerms,
    DocumentPeriod,
    PaymentMeans,
    RequestedMonetaryTotal,
    TaxTotal,
)
from .debit_note_line import DebitNoteLine


class DebitNoteData(BaseModel):
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)

    id: str
    customization_id: DebitNoteCustomizationID
    currency_code: str
    issue_date: date
    issue_time: str
    invoice_period: Optional[DocumentPeriod]
    discrepancy_response: CreditNoteDiscrepancyResponse
    billing_reference: Optional[list[BillingReferenceData]]
    supplier_party: AccountingParty
    customer_party: AccountingParty
    tax_totals: list[TaxTotal]
    lines: list[DebitNoteLine]
    requested_monetary_total: RequestedMonetaryTotal
    payment_means: PaymentMeans
    delivery: Optional[Delivery]
    delivery_terms: Optional[DeliveryTerms]
    note: str
