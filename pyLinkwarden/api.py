from pyLinkwarden.utils.http import Helper
from pyLinkwarden.content import Tags, Links, Collections


class Client:
    """
    Interacts with Linkwarden's API
    """
    def __init__(self, endpoint, access_token=None):
        self.c = Helper(endpoint, headers={'Authorization': f"Bearer {access_token}"} if access_token else None)
        self.tags = Tags(self)
        self.links = Links(self)
        self.collections = Collections(self)
