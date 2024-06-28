import requests


def get_auth_token(self, username: str, password: str, license: str) -> str:
    url = f"{self.base_url}/auth/token"
    payload = {
        'username': username,
        'password': password,
        'license': license
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get('access_token')
