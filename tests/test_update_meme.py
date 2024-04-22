import pytest
import allure
from utils.meme_utils import generate_meme_body

TEST_DATA = [
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    '0123456789',
    '!@#$%^&*()_+-=[]{}|;\':",./<>?',
    ' '
]


@allure.feature('Meme CRUD')
@allure.story('Update')
@pytest.mark.smoke
@allure.title('Обновление мема')
def test_update_meme(get_active_token, change_meme, new_meme):
    payload = generate_meme_body()
    change_meme.update_meme(get_active_token, new_meme.meme_id, payload)
    change_meme.check_status_code(200)
    change_meme.check_response_body(payload)


@allure.feature('Meme CRUD')
@allure.story('Update')
@pytest.mark.regression
@allure.title('Обновление поля tags')
@pytest.mark.parametrize('param', TEST_DATA)
def test_update_tag_param(param, get_active_token, new_meme, change_meme):
    payload = new_meme.json
    payload['tags'].append(param)
    change_meme.update_meme(get_active_token, new_meme.meme_id, payload)
    change_meme.check_status_code(200)


@allure.feature('Meme CRUD')
@allure.story('Update')
@pytest.mark.regression
@allure.title('Обновление поля text')
@pytest.mark.parametrize('param', TEST_DATA)
def test_update_text_param(param, get_active_token, new_meme, change_meme):
    payload = new_meme.json
    payload['text'] = param
    change_meme.update_meme(get_active_token, new_meme.meme_id, payload)
    change_meme.check_status_code(200)


@allure.feature('Meme CRUD')
@allure.story('Update')
@pytest.mark.regression
@allure.title('Обновление поля url')
@pytest.mark.parametrize('param', TEST_DATA)
def test_update_url_param(param, get_active_token, new_meme, change_meme):
    payload = new_meme.json
    payload['url'] = param
    change_meme.update_meme.create_meme(get_active_token, new_meme.meme_id, payload)
    change_meme.check_status_code(200)


@allure.feature('Meme CRUD')
@allure.story('Update')
@pytest.mark.regression
@allure.title('Обновление поля info')
@pytest.mark.parametrize('param', TEST_DATA)
def test_update_info_param(param, get_active_token, new_meme, change_meme):
    payload = new_meme.json
    payload.get('info')['new_obj'] = param
    change_meme.update_meme(get_active_token, new_meme.meme_id, payload)
    change_meme.check_status_code(200)


@allure.feature('Meme CRUD')
@allure.story('Update')
@pytest.mark.regression
@allure.title('Обновление без обязательных полей')
@pytest.mark.parametrize('param', [
    'info',
    'tags',
    'text',
    'url'
])
def test_required_fields(param, get_active_token, new_meme, change_meme):
    payload = new_meme.json
    payload.pop(param, None)
    change_meme.update_meme(get_active_token, new_meme.meme_id, payload)
    change_meme.check_status_code(400)


@allure.feature('Meme CRUD')
@allure.story('Update')
@pytest.mark.regression
@allure.title('Обновление мема без токена')
@pytest.mark.parametrize('headers', [
    {'Content-type': 'application/json', 'Authorization': 'wrong_token'},
    {'Content-type': 'application/json', 'Authorization': ''},
    {'Content-type': 'application/json'}
])
def test_create_meme_without_token(add_meme, new_meme, change_meme, headers):
    change_meme.update_meme("", new_meme.json, headers)
    change_meme.check_status_code(401)
