import requests
from typing import Union
from dte_colombia.client.models import DteApiResult, DTEClientRequest, NumberingRangeRequest
from dte_colombia.data import DEFAULT_HOSTNAME, DEFAULT_HOSTPATH
from dte_colombia.utils import encrypt_with_rsa_public_key


class DTEClient:
    """
    DTE Client to interact with IKU Solutions DTE API.

    Args:
    - api_key: The API key.
    """

    def __init__(self, api_key: str, host: Union[str, None] = None ) -> None:
        self.api_key = api_key
        self.base_url = f"{host}{DEFAULT_HOSTPATH}" if host else f"{DEFAULT_HOSTNAME}{DEFAULT_HOSTPATH}"

    def __get_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def _send(
        self, url: str, payload: DTEClientRequest
    ) -> DteApiResult | Exception:
        headers = self.__get_headers()
        try:
            values = payload.data.model_dump()
            data = encrypt_with_rsa_public_key(values, payload.public_key)
            response = requests.post(url, headers=headers, json=data)
            if response.status_code in [401, 422, 500]:
                raise Exception(response.json())
            return DteApiResult(**response.json())
        except requests.exceptions.RequestException as e:
            raise Exception(e)

    def get_status(
        self, payload: DTEClientRequest
    ) -> DteApiResult | Exception:
        url = f"{self.base_url}/document/status"
        return self._send(url, payload)

    def get_status_zip(
        self, payload: DTEClientRequest
    ) -> DteApiResult | Exception:
        url = f"{self.base_url}/document/zip-status"
        return self._send(url, payload)

    def get_xml_by_key(self, payload: DTEClientRequest) -> DteApiResult | Exception:
        url = f"{self.base_url}/document/xml"
        return self._send(url, payload)

    # def get_exchange_emails(
    #     self, account_info: AccountInfo
    # ) -> DocumentSyncResult | Exception:
    #     url = f"{self.base_url}/service/exchange-emails"
    #     headers = self.__get_headers()
    #     payload = {"account": account_info.model_dump()}

    #     try:
    #         response = requests.post(url, headers=headers, json=payload)
    #         return DocumentSyncResult(**response.json())
    #     except requests.exceptions.RequestException as e:
    #         raise Exception(e)

    def get_numbering_range(self, payload: DTEClientRequest) -> DteApiResult | Exception:
        url = f"{self.base_url}/service/numbering-range"
        return self._send(url, payload)

    def send_invoice(self, payload: DTEClientRequest) -> DteApiResult | Exception:
        url = f"{self.base_url}/documents/sendSalesInvoice"
        return self._send(url, payload)

    def send_credit_note(
        self, payload: DTEClientRequest
    ) -> DteApiResult | Exception:
        url = f"{self.base_url}/documents/sendCreditNote"
        return self._send(url, payload)

    def send_debit_note(
        self, payload: DTEClientRequest
    ) -> DteApiResult | Exception:
        url = f"{self.base_url}/documents/sendDebitNote"
        return self._send(url, payload)

    def send_suport_document(
        self, payload: DTEClientRequest
    ) -> DteApiResult | Exception:
        url = f"{self.base_url}/documents/sendSupportDocument"
        return self._send(url, payload)
