from pydantic import BaseModel

from .extension_amount import ExtensionAmount


class LegalMonetaryTotal(BaseModel):
    line_extension_amount: ExtensionAmount
    tax_exclusive_amount: ExtensionAmount
    tax_inclusive_amount: ExtensionAmount
    payable_amount: ExtensionAmount
