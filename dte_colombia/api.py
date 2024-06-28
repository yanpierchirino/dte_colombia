import requests
from dte_colombia.models.utilities import AccountInfo


class DTEClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "http://127.0.0.1:8000/api/v1"

    def _get_headers(self) -> dict:
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def get_numbering_range(self, resolution_number: str, account_info: AccountInfo) -> dict | None:
        url = f"{self.base_url}/dte/numberingRange"
        payload = {
            "resolution_number": resolution_number,
            "account": account_info
        }
        try:
            response = requests.post(url, headers=self._get_headers(), json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener el rango de numeración: {e}")
            return None

    def get_xml_by_document_key(self, document_key: str, account_info: AccountInfo) -> dict:
        url = f"{self.base_url}/dte/xmlByDocumentKey"
        payload = {
            "documentKey": document_key,
            "account": account_info
        }

        response = requests.post(url, headers=self._get_headers(), json=payload)
        response.raise_for_status()
        return response.json()
