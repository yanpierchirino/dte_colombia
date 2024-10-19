from enum import Enum


class TaxLevelCode(str, Enum):
    """Tax level codes for organizations."""

    MAJOR_CONTRIBUTOR = "O-12"  # Gran contribuyente
    SELF_RETAINER = "O-15"  # Autorretenedor
    VAT_RETENTION_AGENT = "O-23"  # Agente de retención IVA
    SIMPLE_TAX_REGIME = "O-47"  # Régimen simple de tributación
    OTHER = "R-99-PN"  # No aplica – Otros *
