from pydantic import BaseModel

from .credit_note import CreditNoteData
from .debit_note import DebitNoteData
from .sales_invoice import SalesInvoiceData
from .support_document import SupportDocumentData
from .v1_api_account import AccountInfo


class DTEClientRequest(BaseModel):
    data: dict
    public_key: str


class SalesInvoiceRequest(BaseModel):
    invoice: SalesInvoiceData
    account: AccountInfo


class CeditnoteRequest(BaseModel):
    credit_note: CreditNoteData
    account: AccountInfo


class DebitNoteRequest(BaseModel):
    debit_note: DebitNoteData
    account: AccountInfo


class SupportDocumentRequest(BaseModel):
    document: SupportDocumentData
    account: AccountInfo


class DocumentRequest(BaseModel):
    id: str
    account: AccountInfo
