import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class GetMemeById(BaseEndpoint):
    _endpoint = '/meme/'

    @allure.step('Get meme by id')
    def get_meme_by_id(self, token, meme_id, headers=None):
        self._headers['Authorization'] = token
        headers = headers if headers else self._headers
        self.response = requests.get(
            f'{self._base_url}{self._endpoint}{meme_id}',
            headers=headers
        )
        self.json = self.response.json() if self.response.status_code == 200 else None
