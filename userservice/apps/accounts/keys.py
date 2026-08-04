from __future__ import annotations

import base64
import hashlib

from django.conf import settings
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def _b64url_uint(value: int) -> str:
    raw = value.to_bytes((value.bit_length() + 7) // 8, "big")
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def private_key():
    path = settings.JWT_KEY_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        path.write_bytes(
            key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
        return key
    return serialization.load_pem_private_key(path.read_bytes(), password=None)


def public_key_pem() -> str:
    return (
        private_key()
        .public_key()
        .public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        .decode("ascii")
    )


def key_id() -> str:
    digest = hashlib.sha256(public_key_pem().encode("ascii")).hexdigest()
    return digest[:16]


def jwk() -> dict:
    numbers = private_key().public_key().public_numbers()
    return {
        "kty": "RSA",
        "use": "sig",
        "kid": key_id(),
        "alg": settings.JWT_ALGORITHM,
        "n": _b64url_uint(numbers.n),
        "e": _b64url_uint(numbers.e),
    }
