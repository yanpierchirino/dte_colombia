from pydantic import BaseModel


class DocumentUUID(BaseModel):
    name: str
    content: str


class CompanyID(BaseModel):
    id: str
    name: str
    content: str


class TaxLevelCode(BaseModel):
    name: str
    code: str


class TaxScheme(BaseModel):
    id: str
    name: str


class PartyTaxScheme(BaseModel):
    name: str
    company_id: CompanyID
    tax_level_code: TaxLevelCode
    tax_scheme: TaxScheme


class SenderParty(BaseModel):
    party_tax_scheme: PartyTaxScheme


class ReceiverParty(BaseModel):
    party_tax_scheme: PartyTaxScheme


class ExternalReference(BaseModel):
    description: str


class Attachment(BaseModel):
    external_reference: ExternalReference


class ResultOfVerification(BaseModel):
    validation_result_code: str
    validation_date: str
    validation_time: str


class DocumentReference(BaseModel):
    id: str
    uuid: DocumentUUID
    issue_date: str
    attachment: Attachment
    result_of_verification: ResultOfVerification


class ParentDocumentLineReference(BaseModel):
    line_id: str = "1"
    document_reference: DocumentReference
