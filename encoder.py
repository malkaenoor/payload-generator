import base64
import urllib.parse
import html

class Encoder:

    def encode(self, payload, method):
        if method == "base64":
            return self.base64_encode(payload)

        elif method == "url":
            return self.url_encode(payload)

        elif method == "html":
            return self.html_encode(payload)

        else:
            return None

    def base64_encode(self, payload):
        try:
            encoded = base64.b64encode(payload.encode()).decode()
            return encoded
        except:
            return None

    def url_encode(self, payload):
        try:
            return urllib.parse.quote(payload)
        except:
            return None

    def html_encode(self, payload):
        try:
            return html.escape(payload)
        except:
            return None
