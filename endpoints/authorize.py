import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class Authorize(BaseEndpoint):
    _endpoint = '/authorize'
    token = None
    user = None

    @allure.step('Get authorize token')
    def authorize(self, payload, headers=None):
        headers = headers if headers else self._headers
        self.response = requests.post(
            f'{self._base_url}{self._endpoint}',
            json=payload,
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.token = self.json['token']
            self.user = self.json['user']

    @allure.step('Check response auth body')
    def check_auth_response_body(self, name_param):
        assert self.user == name_param['name'], \
            f'response body {self.user} is not {name_param['name']}'
        assert self.token is not None
