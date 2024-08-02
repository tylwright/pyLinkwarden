import json

class Tags:
    def __init__(self, client):
        self.c = client.c
        self.TAGS_PATH = '/api/v1/tags'

    def _get_raw(self):
        """
        Returns entirety of tags endpoint response.

        :return: Requests library response object
        """
        return self.c._get(path=self.TAGS_PATH)

    def _get(self):
        """
        Returns JSON of tags endpoint response.

        :return: JSON of link data
        """
        response = self._get_raw()
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch data: {response.status_code}")
        
        data = response.json().get('response', [])

        return data

    def list(self):
        """
        Returns list of tags

        :returns: List of tags
        """
        return [tag['name'] for tag in self._get()]

    def rename(self, tag_id, new_name):
        """
        Renames a tag

        :param tag_id: Id of tag you wish to rename
        :param new_name: New name for tag to be renamed to
        :returns: Requests library response object
        """
        path = f"{self.TAGS_PATH}/{tag_id}"
        return self.c._put(path=path, data={'name': new_name})

    def delete(self, tag_id):
        """
        Deletes a tag
        
        :param tag_id: Id of tag you wish to delete
        :returns: Requests library response object
        """
        path = f"{self.TAGS_PATH}/{tag_id}"
        return self.c._delete(path=path)


class Links:
    def __init__(self, client):
        self.c = client.c
        self.LINKS_PATH = '/api/v1/links'

    def _get_raw(self, link_id=None):
        """
        Returns entirety of links endpoint response.
        Returns all links if link_id not specified.
        Otherwise, returns specific link.

        :param link_id: Id of link that you wish to view.  Optional.
        :return: Requests library response object
        """
        if link_id:
            path = f"{self.LINKS_PATH}/{link_id}"
        else:
            path = self.LINKS_PATH
        return self.c._get(path=path)

    def _get(self, link_id=None, specific_attribute=None):
        """
        Returns JSON of links endpoint response.
        Returns all links if link_id is not specified.
        Otherwise, returns the specific link.

        :param link_id: Id of the link that you wish to view. Optional.
        :param specific_attribute: Returns the value of this attribute. Optional.
        :return: JSON of link data or the specific attribute's value.
        """
        response = self._get_raw(link_id)
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch data: {response.status_code}")
        
        data = response.json().get('response', [])

        if specific_attribute:
            if link_id is not None:
                return data.get(specific_attribute) if isinstance(data, dict) else None
            else:
                return [link.get(specific_attribute) for link in data if isinstance(link, dict) and specific_attribute in link]
        else:
            return data

    def list_all_urls(self):
        """
        Lists all URLs in Linkwarden.
        
        :returns: List of URLs
        """
        return self._get(specific_attribute='url')

    def check_if_url_exists(self, url):
        """
        Checks to see if the provided URL already exists.

        :param url: URL of page
        :returns: True if page exists, False if page does not exist.
        """
        all_urls = self.list_all_urls()
        for u in all_urls:
            if u == url:
                return True
        return False

    def list(self):
        """
        Returns list of links

        :return: List of titles of links.
        """
        return self._get(specific_attribute='name')

    def delete(self, link_id):
        """
        Deletes a link
        
        :param link_id: Id of link you wish to delete
        :returns: Requests library response object
        """
        path = f"{self.LINKS_PATH}/{link_id}"
        return self.c._delete(path=path)


class Collections:
    def __init__(self, client):
        self.c = client.c
        self.COLLECTIONS_PATH = '/api/v1/collections'

    def _get_raw(self):
        """
        Returns entirety of collections endpoint response.

        :return: Requests library response object
        """
        return self.c._get(path=self.COLLECTIONS_PATH)

    def _get(self):
        """
        Returns JSON of collections endpoint response.

        :return: JSON of link data
        """
        response = self._get_raw()
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch data: {response.status_code}")
        
        data = response.json().get('response', [])

        return data

    def list(self):
        """
        Returns list of collections

        :returns: List of collections
        """
        return [tag['name'] for tag in self._get()]

    def delete(self, collection_id):
        """
        Deletes a collection
        
        :param collection_id: Id of collection you wish to delete
        :returns: Requests library response object
        """
        path = f"{self.COLLECTIONS_PATH}/{collection_id}"
        return self.c._delete(path=path)
