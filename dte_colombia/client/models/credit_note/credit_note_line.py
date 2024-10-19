from pydantic import BaseModel

from ..components import ExtensionAmount, Item, Price, Quantity, TaxTotal


class CreditNoteLine(BaseModel):
    id: int
    quantity: Quantity
    line_extension_amount: ExtensionAmount
    tax_totals: list[TaxTotal]
    item: Item
    price: Price
