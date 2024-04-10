import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class TokenIsLive(BaseEndpoint):
    _endpoint = '/authorize/'
    text = None

    @allure.step('Check token is live')
    def check_token(self, token, headers=None):
        headers = headers if headers else self._headers
        self.response = requests.get(
            f'{self._base_url}{self._endpoint}{token}',
            headers=headers
        )
        self.text = self.response.text
