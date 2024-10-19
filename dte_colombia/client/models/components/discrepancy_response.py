from pydantic import BaseModel, ConfigDict

from dte_colombia.client.enums import CreditNoteDiscrepancyCode


class CreditNoteDiscrepancyResponse(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    reference_id: str
    response_code: CreditNoteDiscrepancyCode
    description: str
