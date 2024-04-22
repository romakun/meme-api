import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAllMeme(BaseEndpoint):
    _endpoint = '/meme'

    @allure.step('Get all meme')
    def get_all_meme(self, token, headers=None):
        self._headers['Authorization'] = token
        headers = headers if headers else self._headers
        self.response = requests.get(
            f'{self._base_url}{self._endpoint}',
            headers=headers
        )
        self.json = self.response.json() if self.response.status_code == 200 else None

    @allure.step('Check meme count')
    def check_meme_count(self, new_meme_count):
        assert len(self.json['data']) == new_meme_count, \
            f'meme count {len(self.json['data'])} is not equal or more than {new_meme_count}'

    @allure.step('Check meme body')
    def check_meme_body(self, meme):
        response_meme = None
        for item in self.json['data']:
            if item['id'] == meme['id']:
                response_meme = item
                break
        assert response_meme == meme, \
            f'response body {response_meme} is not {meme}'
