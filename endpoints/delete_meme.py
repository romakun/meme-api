import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    _endpoint = '/meme/'

    @allure.step('Delete meme by id')
    def delete_meme(self, token, meme_id, headers=None):
        self._headers['Authorization'] = token
        headers = headers if headers else self._headers
        self.response = requests.delete(
            f'{self._base_url}{self._endpoint}{meme_id}',
            headers=headers
        )