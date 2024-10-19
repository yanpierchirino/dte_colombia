from enum import Enum


class InvoiceTypeCode(str, Enum):
    """Invoice type codes for invoices."""

    SALES_INVOICE = "01"  # Factura electrónica de Venta
    EXPORT_SALES_INVOICE = "02"  # Factura electrónica de venta ‐ exportación
    TRANSCRIPTION_INVOICE = "03"  # Transcripción de la factura de talonrio o papel
    SALES_INVOICE_TYPE_04 = "04"  # Factura electrónica de Venta ‐ tipo 04
    SUPPORT_DOCUMENT = "05"  # Documento soporte en adquisiciones efectuadas a sujetos no obligados a expedir factura o documento equivalente


class CreditNoteTypeCode(str, Enum):
    """Credit note type codes for credit notes."""

    CREDIT_NOTE = "91"  # Nota Crédito
    SUPPORT_DOCUMENT_CREDIT_NOTE = "95"  # Nota de ajuste al documento soporte en adquisiciones efectuadas a sujetos no obligados a expedir factura o documento equivalente


class DebitNoteTypeCode(str, Enum):
    """Debit note type codes for debit notes."""

    DEBIT_NOTE = "92"  # Nota Débito
