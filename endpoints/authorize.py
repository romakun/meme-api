import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class Authorize(BaseEndpoint):
    _endpoint = '/authorize'

    @allure.step('Get authorize token')
    def authorize(self, payload, headers=None):
        headers = headers if headers else self._headers
        self.response = requests.post(
            f'{self._base_url}{self._endpoint}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.token = self.json['token']
        self.user = self.json['user']
