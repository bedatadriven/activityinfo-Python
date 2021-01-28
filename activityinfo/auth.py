from requests.auth import AuthBase


class TokenAuth(AuthBase):
    """Authentication using a token"""
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = self.token
        return r
