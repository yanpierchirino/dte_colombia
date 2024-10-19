import base64
import json

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def encrypt_with_rsa_public_key(data: dict, dte_public_key: str) -> dict:
    """
    Encripta un objeto JSON con una clave pública utilizando RSA y lo codifica en base64.

    :param data: Diccionario de datos que será encriptado.
    :param public_key_pem: Clave pública en formato PEM.
    :return: String encriptado y codificado en base64.
    """
    # Serializar la clave pública
    public_key_pem = base64.b64decode(dte_public_key)
    public_key = serialization.load_pem_public_key(public_key_pem)

    # Convertir el objeto JSON en una cadena
    ciphertext, cipher = encrypt_with_aes_standardized(json.dumps(data))
    json_data = json.dumps(cipher).encode("utf-8")

    # Encriptar los datos JSON usando la clave pública
    encrypted_data = public_key.encrypt(
        json_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None,
        ),
    )

    # Codificar los datos en base64
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode("utf-8")
    ciphertext_data_base64 = base64.b64encode(ciphertext).decode("utf-8")
    return {"data": f"{encrypted_data_base64}:::{ciphertext_data_base64}"}


def encrypt_with_aes_standardized(data: str, bytes_len: int = 32) -> tuple:
    key = get_random_bytes(bytes_len)
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return ciphertext, {
        "key": base64.b64encode(key).decode(),
        "nonce": base64.b64encode(nonce).decode(),
        "tag": base64.b64encode(tag).decode(),
    }
