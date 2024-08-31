import requests

from dte_colombia.data.constants import BASE_URL, INVOICE_RESOLUTION_MAP
from dte_colombia.schemas.common.response import Response
from dte_colombia.schemas.utilities import AccountInfo, InvoiceResolution


class DTEClient:
    """
    DTE Client to interact with the DTE API.

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

    def get_numbering_range(
        self, resolution_number: str, account_info: AccountInfo
    ) -> Response | Exception:
        url = f"{self.base_url}/numberingRange"
        headers = self.__get_headers()
        payload = {
            "resolution_number": resolution_number,
            "account": account_info.model_dump(),
        }
        try:
            result = requests.post(url, headers=headers, json=payload)
            response = Response(**result.json())
            if response.success and isinstance(response.data, dict):
                resolution = {}
                for key in response.data.keys():
                    resolution[INVOICE_RESOLUTION_MAP[key]] = response.data[key]
                response.data = InvoiceResolution(**resolution)
            return Response(**result.json())
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def get_xml_by_document_key(
        self, document_key: str, account_info: AccountInfo
    ) -> Response | Exception:
        url = f"{self.base_url}/xmlByDocumentKey"
        headers = self.__get_headers()
        payload = {"documentKey": document_key, "account": account_info.model_dump()}

        try:
            response = requests.post(url, headers=headers, json=payload)
            return Response(**response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def get_exchange_emails(self, account_info: AccountInfo) -> Response | Exception:
        url = f"{self.base_url}/exchangeEmails"
        headers = self.__get_headers()
        payload = {"account": account_info.model_dump()}

        try:
            response = requests.post(url, headers=headers, json=payload)
            return Response(**response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(e)
