import requests

class Client:
    """Client to interact with the ActivityInfo API."""

    base_url = 'https://www.activityinfo.org/'

    def __init__(self, username, password):
        self.auth = requests.auth.HTTPBasicAuth(username=username, password=password)
        self.path = self.base_url + 'resources/'

    def get(self, resource_path, query_params=None):
        r = requests.get(url=self.path + resource_path, params=query_params, auth=self.auth)
        r.raise_for_status()
        return r.json()

    # TODO: put().