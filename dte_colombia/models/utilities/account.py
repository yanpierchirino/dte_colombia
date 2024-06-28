from typing import Optional
from pydantic import BaseModel


class AccountInfo(BaseModel):
    """
    Account information required for DTE operations.
    
    Attributes:
    
    - profile_execution_id: The profile execution ID.
    - test_set_id: The test set ID.
    - company_vat: The company VAT [NIT, CC, CE, Etc...].
    - software_id: The software ID.
    - software_security_code: The software security code.
    - technical_key: The technical key.
    - certificate: The certificate (.pfx Base64 encoded).
    - certificate_pass: The certificate password.
    """
    profile_execution_id: int
    test_set_id: Optional[str]
    company_vat: str
    software_id: str
    software_security_code: str
    technical_key: Optional[str]
    certificate: str
    certificate_pass: str
