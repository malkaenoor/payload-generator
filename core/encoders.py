import base64
import urllib.parse

def to_base64(s: str) -> str:
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def from_base64(s: str) -> str:
    return base64.b64decode(s.encode('utf-8')).decode('utf-8')

def url_encode(s: str) -> str:
    return urllib.parse.quote_plus(s)

def url_decode(s: str) -> str:
    return urllib.parse.unquote_plus(s)

def to_hex(s: str) -> str:
    return s.encode('utf-8').hex()

def from_hex(h: str) -> str:
    return bytes.fromhex(h).decode('utf-8')

def to_unicode_escape(s: str) -> str:
    # returns unicode escape sequence representation
    return s.encode('unicode_escape').decode('ascii')

def from_unicode_escape(s: str) -> str:
    return s.encode('ascii').decode('unicode_escape')
