from enum import Enum


class CreditNoteDiscrepancyCode(str, Enum):
    """Discrepancy codes for credit notes."""

    PARTIAL_REFUND = (
        "1"  # Devolución parcial de los bienes y/o no aceptación parcial del servicio
    )
    INVOICE_CANCELATION = "2"  # Anulación de factura electrónica
    PARTIAL_DISCOUNT = "3"  # Rebaja  o descuento parcial o total
    PRICE_ADJUSTMENT = "4"  # Ajuste de precio
    COMMERCIAL_DISCOUNT = "5"  # Descuento comercial por pronto pago
    VOLUME_DISCOUNT = "6"  # Descuento comercial por volumen de ventas
