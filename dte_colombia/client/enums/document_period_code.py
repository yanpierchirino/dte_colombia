from enum import Enum


class InvoicePeriodCode(str, Enum):
    """Period codes for invoices."""

    PER_OPERATION = "1"  # Por operación
    WEEKLY_ACCUMULATED = "2"  # Acumulado semanal
