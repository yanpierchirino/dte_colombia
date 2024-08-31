from datetime import date

from pydantic import BaseModel


class InvoiceResolution(BaseModel):
    serie: str
    range_from: int
    range_end: int
    resolucion_date: date
    date_start: date
    date_end: date
    technical_key: str
    state: str
