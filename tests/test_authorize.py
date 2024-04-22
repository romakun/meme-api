import pytest
import allure


@allure.feature('Auth')
@allure.story('Token')
@pytest.mark.smoke
@allure.title('Получение токена')
def test_authorize_token(auth, get_all):
    payload = {'name': 'roma_kun'}
    auth.authorize(payload)
    auth.check_status_code(200)
    auth.check_auth_response_body(payload)
    get_all.get_all_meme(auth.token)
    get_all.check_status_code(200)


@allure.feature('Auth')
@allure.story('Token')
@pytest.mark.regression
@allure.title('Получение токена без имени пользователя')
def test_authorize_token_without_user(auth):
    payload = {'name': ''}
    auth.authorize(payload)
    auth.check_status_code(400)


@allure.feature('Auth')
@allure.story('Token')
@pytest.mark.regression
@allure.title('Получение токена с пустым телом')
def test_authorize_token_with_empty_body(auth):
    payload = {}
    auth.authorize(payload)
    auth.check_status_code(400)
