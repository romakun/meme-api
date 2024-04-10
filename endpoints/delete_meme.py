import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    endpoint = '/meme/'
    meme_id = None
