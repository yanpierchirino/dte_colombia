from typing import Optional, Union

from pydantic import BaseModel


class EnvelopeHeaderSecurityTimestamp(BaseModel):
    created: str
    expires: str


class Timestamp(BaseModel):
    created: str
    expires: str


class ErrorMessages(BaseModel):
    messages: Optional[list[str]]


class DocumentSyncResult(BaseModel):
    error_messages: Union[ErrorMessages, dict]
    is_valid: bool
    status_code: str
    status_description: str
    status_message: Union[str, dict]
    xml_base64_bytes: Union[str, dict]
    xml_bytes: Union[str, dict]
    xml_document_key: Union[str, dict]
    xml_file_name: str
    timestamp: Union[EnvelopeHeaderSecurityTimestamp, Timestamp]
    trackId: Optional[str]
