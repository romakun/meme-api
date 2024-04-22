import allure
import requests
import os

from endpoints.base_endpoint import BaseEndpoint


class CreateMeme(BaseEndpoint):
    _endpoint = '/meme'
    meme_id = None

    @allure.step('Add meme')
    def create_meme(self, token, payload, headers=None):
        self._headers['Authorization'] = token
        headers = headers if headers else self._headers
        self.response = requests.post(
            f'{self._base_url}{self._endpoint}',
            json=payload,
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.meme_id = self.json['id']

    @allure.step('Check created meme body')
    def check_created_meme_body(self, expected_body):
        assert 'id' in self.json and self.json['id'] is not None
        assert 'updated_by' in self.json and self.json['updated_by'] == os.getenv('USER')
        self.json.pop('id', None)
        self.json.pop('updated_by', None)
        assert self.json == expected_body, \
            f'response body {self.json} is not {expected_body}'
