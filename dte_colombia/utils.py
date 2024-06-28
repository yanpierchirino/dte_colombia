import requests

from dte_colombia.constants import BASE_URL


def get_auth_token(username: str, password: str, license: str) -> str:
    """
    Get the authentication token for the API.

    Args:
    - username: The username.
    - password: The password.
    - license: The license.
    """
    url = f"{BASE_URL}/auth/token"
    payload = {"username": username, "password": password, "license": license}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get("access_token")
