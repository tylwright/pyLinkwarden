import requests


class Helper:
    """
    HTTP client to make API calls to Linkwarden
    """
    def __init__(self, endpoint, params=None, headers=None):
        self.endpoint = endpoint
        self.params = params or {}
        self.headers = headers or {}

    def _merge_dicts(self, base_dict, additional_dict):
        """
        Merges two dictionaries, giving precedence to the additional_dict.
        """
        return {**base_dict, **(additional_dict or {})}

    def _request(self, method, path, params=None, headers=None, data=None, **kwargs):
        """
        General method to handle HTTP requests
        """
        url = f"{self.endpoint}{path}"
        all_params = self._merge_dicts(self.params, params)
        all_headers = self._merge_dicts(self.headers, headers)
        return requests.request(method, url, params=all_params, headers=all_headers, data=data, **kwargs)

    def _get(self, path, params=None, headers=None):
        """
        Call GET against a URL
        """
        return self._request('GET', path, params=params, headers=headers)

    def _post(self, path, data=None, params=None, headers=None):
        """
        Call POST against a URL
        """
        return self._request('POST', path, data=data, params=params, headers=headers)

    def _put(self, path, data=None, params=None, headers=None):
        """
        Call PUT against a URL
        """
        return self._request('PUT', path, data=data, params=params, headers=headers)

    def _delete(self, path, params=None, headers=None, data=None):
        """
        Call DELETE against a URL
        """
        return self._request('DELETE', path, params=params, headers=headers, data=data)

    def _patch(self, path, data=None, params=None, headers=None):
        """
        Call PATCH against a URL
        """
        return self._request('PATCH', path, data=data, params=params, headers=headers)

    def _head(self, path, params=None, headers=None):
        """
        Call HEAD against a URL
        """
        return self._request('HEAD', path, params=params, headers=headers)

    def _options(self, path, params=None, headers=None):
        """
        Call OPTIONS against a URL
        """
        return self._request('OPTIONS', path, params=params, headers=headers)
