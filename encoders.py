# encoders.py
import base64
import urllib.parse
import binascii

def encode_base64(s: str) -> str:
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def encode_url(s: str) -> str:
    return urllib.parse.quote_plus(s)

def encode_hex(s: str) -> str:
    return binascii.hexlify(s.encode('utf-8')).decode('utf-8')

def encode_unicode_escape(s: str) -> str:
    return s.encode('unicode_escape').decode('ascii')

ENCODERS = {
    "base64": encode_base64,
    "url": encode_url,
    "hex": encode_hex,
    "unicode": encode_unicode_escape,
}
