from pydantic import BaseModel, ConfigDict

from ..components import ExtensionAmount, Item, Price, Quantity, TaxTotal


class DebitNoteLine(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    quantity: Quantity
    line_extension_amount: ExtensionAmount
    tax_total: list[TaxTotal]
    item: Item
    price: Price
