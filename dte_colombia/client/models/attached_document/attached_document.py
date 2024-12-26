from pydantic import BaseModel
from .components import SenderParty, ReceiverParty, ParentDocumentLineReference


class AttachedDocument(BaseModel):
    profile_execution_id: str
    id: str
    issue_date: str
    issue_time: str
    parent_document_id: str
    sender_party: SenderParty
    receiver_party: ReceiverParty
    parent_document_reference: ParentDocumentLineReference
