from typing import Optional

from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    telephone: str
    telefax: Optional[str] = None
    electronic_mail: str
    note: str
