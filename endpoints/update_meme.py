import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class UpdateMeme(BaseEndpoint):
    _endpoint = '/meme/'

    @allure.step('Update meme by id')
    def update_meme(self, token, meme_id, payload, headers=None):
        self._headers['Authorization'] = token
        headers = headers if headers else self._headers
        self.response = requests.put(
            f'{self._base_url}{self._endpoint}{meme_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json() if self.response.status_code == 200 else None
