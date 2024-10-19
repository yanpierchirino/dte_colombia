from pydantic import BaseModel

from .extension_amount import ExtensionAmount
from .tax import TaxCategory


class TaxSubtotal(BaseModel):
    taxable_amount: ExtensionAmount
    tax_amount: ExtensionAmount
    tax_category: TaxCategory


class TaxTotal(BaseModel):
    tax_amount: ExtensionAmount
    tax_evidence_indicator: bool = False
    tax_subtotals: list[TaxSubtotal]
