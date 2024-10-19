from enum import Enum


class InvoiceCustomizationID(str, Enum):
    """Customization ID for invoices."""

    AIU = "09"
    STANDARD = "10"
    MANDATES = "11"
    TRANSPORT = "12"
    EXCHANGE = "13"


class CreditNoteCustomizationID(str, Enum):
    """Customization ID for credit notes."""

    REFERENCED = "20"  # Nota Crédito con referencia a una factura electrónica
    NO_REFERENCED = "22"  # Nota Crédito sin referencia a una factura electrónica


class DebitNoteCustomizationID(str, Enum):
    """Customization ID for debit notes."""

    REFERENCED = "30"  # Nota Débito con referencia a una factura electrónica
    NO_REFERENCED = "32"  # Nota Débito sin referencia a una factura electrónica
