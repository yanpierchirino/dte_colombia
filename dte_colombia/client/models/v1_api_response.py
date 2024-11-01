from typing import Optional, Union

from pydantic import BaseModel


class Timestamp(BaseModel):
    created: str
    expires: str


class ErrorMessages(BaseModel):
    messages: Optional[list[str]]


class DteApiResult(BaseModel):
    is_valid: Optional[bool] = None
    status_code: Optional[str] = None
    status_description: Optional[str] = None
    status_message: Optional[Union[str, dict]] = None
    xml_base64_bytes: Optional[Union[str, dict]] = None
    xml_bytes: Optional[Union[str, dict]] = None
    xml_document_key: Optional[Union[str, dict]] = None
    xml_file_name: Optional[str] = None
    error_messages: Optional[Union[ErrorMessages, dict]] = None
    timestamp: Optional[Timestamp] = None
    trackId: Optional[str] = None
