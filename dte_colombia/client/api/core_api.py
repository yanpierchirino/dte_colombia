import requests

from dte_colombia.client.models import AccountInfo, DocumentSyncResult, DTEClientRequest
from dte_colombia.data import BASE_URL
from dte_colombia.utils import encrypt_with_rsa_public_key


class DTEClient:
    """
    DTE Client to interact with IKU Solutions DTE API.

    Args:
    - api_key: The API key.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = BASE_URL

    def __get_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def _send(
        self, url: str, payload: DTEClientRequest
    ) -> DocumentSyncResult | Exception:
        headers = self.__get_headers()
        try:
            data = encrypt_with_rsa_public_key(payload.data, payload.public_key)
            response = requests.post(url, headers=headers, json=data)
            if response.status_code in [401, 422, 500]:
                raise Exception(response.json())
            return DocumentSyncResult(**response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    # def get_numbering_range(
    #     self, resolution_number: str, account_info: AccountInfo
    # ) -> DocumentSyncResult | Exception:
    #     url = f"{self.base_url}/customerServices/numberingRange"
    #     headers = self.__get_headers()
    #     payload = {
    #         "resolution_number": resolution_number,
    #         "account": account_info.model_dump(),
    #     }
    #     try:
    #         result = requests.post(url, headers=headers, json=payload)
    #         response = DocumentSyncResult(**result.json())
    #         if response.success and isinstance(response.data, dict):
    #             response.data = InvoiceResolution(**response.data).model_dump()
    #         return response
    #     except requests.exceptions.RequestException as e:
    #         raise Exception(e)

    def get_xml_by_document_key(
        self, document_key: str, account_info: AccountInfo
    ) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/customerServices/xmlByDocumentKey"
        headers = self.__get_headers()
        payload = {"documentKey": document_key, "account": account_info.model_dump()}

        try:
            response = requests.post(url, headers=headers, json=payload)
            return DocumentSyncResult(**response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def get_exchange_emails(
        self, account_info: AccountInfo
    ) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/customerServices/exchangeEmails"
        headers = self.__get_headers()
        payload = {"account": account_info.model_dump()}

        try:
            response = requests.post(url, headers=headers, json=payload)
            return DocumentSyncResult(**response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def send_invoice(self, payload: DTEClientRequest) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/documents/sendSalesInvoice"
        return self._send(url, payload)

    def send_credit_note(
        self, payload: DTEClientRequest
    ) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/documents/sendCreditNote"
        return self._send(url, payload)

    def send_debit_note(
        self, payload: DTEClientRequest
    ) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/documents/sendDebitNote"
        return self._send(url, payload)

    def send_suport_document(
        self, payload: DTEClientRequest
    ) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/documents/sendSupportDocument"
        return self._send(url, payload)

    def check_zip_status(
        self, payload: DTEClientRequest
    ) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/documents/billZipStatus"
        return self._send(url, payload)

    def check_status_by_uuid(
        self, payload: DTEClientRequest
    ) -> DocumentSyncResult | Exception:
        url = f"{self.base_url}/customerServices/statusByKey"
        return self._send(url, payload)
