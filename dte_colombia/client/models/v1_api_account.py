from typing import Optional

from pydantic import BaseModel, ConfigDict

from dte_colombia.client.enums import ProfileExcecutionId, TaxIdentifierType


class AccountInfo(BaseModel):
    """
    Account information required for DTE operations.

    Attributes:

    - profile_execution_id: The profile execution ID.
    - company_verification_digit: The company identifier verification digit.
    - company_identification_type: The company identification type.
    - company_identification: The company identification.
    - test_set_id: The test set ID.
    - software_id: The software ID.
    - software_security_code: The software security code.
    - technical_key: The technical key.
    - certificate: The certificate (.pfx Base64 encoded).
    - certificate_pass: The certificate password.
    """

    model_config = ConfigDict(use_enum_values=True)

    profile_execution_id: ProfileExcecutionId
    company_verification_digit: int
    company_identification_type: TaxIdentifierType
    company_identification: str
    software_id: str
    software_security_code: str
    technical_key: str
    certificate_pass: str
    certificate: str
    test_set_id: Optional[str] = None
