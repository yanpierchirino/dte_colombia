from pydantic import BaseModel

from dte_colombia.schemas.utilities import InvoiceResolution


class Response(BaseModel):
    success: bool
    message: str
    data: dict | InvoiceResolution
