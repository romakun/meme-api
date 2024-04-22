import allure
import dotenv
import os


class BaseEndpoint:
    dotenv.load_dotenv()
    _base_url = os.getenv("URL_API")
    _headers = {'Content-type': 'application/json'}
    response = None
    json = None

    @allure.step('Check response status code')
    def check_status_code(self, code):
        assert self.response.status_code == code, f'status code {self.response.status_code} is not {code}'

    @allure.step('Check response meme body')
    def check_response_body(self, expected_body):
        assert self.response.json() == expected_body, \
            f'response body {self.response.json()} is not {expected_body}'
