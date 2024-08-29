from dte_colombia.core import DTEClient
from dte_colombia.schemas.utilities import AccountInfo

client = DTEClient(
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDcyMjcwMjksInVpZCI6MiwicGFydG5lcl9pZCI6MywidXNlcm5hbWUiOiJzdXBwb3J0QHlhbmNoaXJpbm8uY29tIiwibGljZW5zZSI6InFhenhzdyJ9.Cu0kVKd_3hx81mhp08m7Pn0oxUUc1C5XvJYUwQGHH50"
)
account = AccountInfo.model_validate(
    {
        "profile_execution_id": 1,
        "test_set_id": "string",
        "company_vat": "9011060908",
        "software_id": "9cc37784-93f7-4f44-9e54-098d2066be02",
        "software_security_code": "3343",
        "technical_key": "string",
        "certificate": "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",
        "certificate_pass": "vhfszPCDXV",
    }
)
client.get_exchange_emails(account_info=account)
print(client)
