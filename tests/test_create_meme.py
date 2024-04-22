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
@allure.story('Create')
@pytest.mark.smoke
@allure.title('Создание мема')
def test_create_meme(get_active_token, add_meme, remove_meme):
    try:
        payload = generate_meme_body()
        add_meme.create_meme(get_active_token, payload)
        add_meme.check_status_code(200)
        add_meme.check_created_meme_body(payload)
    finally:
        remove_meme.delete_meme(get_active_token, add_meme.meme_id)


@allure.feature('Meme CRUD')
@allure.story('Create')
@pytest.mark.regression
@allure.title('Проверка поля tag')
@pytest.mark.parametrize('param', TEST_DATA)
def test_tag_param(param, get_active_token, add_meme, remove_meme):
    try:
        payload = generate_meme_body()
        payload['tags'].append(param)
        add_meme.create_meme(get_active_token, payload)
        add_meme.check_status_code(200)
    finally:
        remove_meme.delete_meme(get_active_token, add_meme.meme_id)


@allure.feature('Meme CRUD')
@allure.story('Create')
@pytest.mark.regression
@allure.title('Проверка поля text')
@pytest.mark.parametrize('param', TEST_DATA)
def test_text_param(param, get_active_token, add_meme, remove_meme):
    try:
        payload = generate_meme_body()
        payload['text'] = param
        add_meme.create_meme(get_active_token, payload)
        add_meme.check_status_code(200)
    finally:
        remove_meme.delete_meme(get_active_token, add_meme.meme_id)


@allure.feature('Meme CRUD')
@allure.story('Create')
@pytest.mark.regression
@allure.title('Проверка поля url')
@pytest.mark.parametrize('param', TEST_DATA)
def test_url_param(param, get_active_token, add_meme, remove_meme):
    try:
        payload = generate_meme_body()
        payload['url'] = param
        add_meme.create_meme(get_active_token, payload)
        add_meme.check_status_code(200)
    finally:
        remove_meme.delete_meme(get_active_token, add_meme.meme_id)


@allure.feature('Meme CRUD')
@allure.story('Create')
@pytest.mark.regression
@allure.title('Проверка поля info')
@pytest.mark.parametrize('param', TEST_DATA)
def test_info_param(param, get_active_token, add_meme, remove_meme):
    try:
        payload = generate_meme_body()
        payload.get('info')['new_obj'] = param
        add_meme.create_meme(get_active_token, payload)
        add_meme.check_status_code(200)
    finally:
        remove_meme.delete_meme(get_active_token, add_meme.meme_id)


@allure.feature('Meme CRUD')
@allure.story('Create')
@pytest.mark.regression
@allure.title('Создание без обязательных полей')
@pytest.mark.parametrize('param', [
    'info',
    'tags',
    'text',
    'url'
])
def test_required_fields(param, get_active_token, add_meme):
    payload = generate_meme_body()
    payload.pop(param, None)
    add_meme.create_meme(get_active_token, payload)
    add_meme.check_status_code(400)


@allure.feature('Meme CRUD')
@allure.story('Create')
@pytest.mark.regression
@allure.title('Создание мема без токена')
@pytest.mark.parametrize('headers', [
    {'Content-type': 'application/json', 'Authorization': 'wrong_token'},
    {'Content-type': 'application/json', 'Authorization': ''},
    {'Content-type': 'application/json'}
])
def test_create_meme_without_token(add_meme, headers):
    payload = generate_meme_body()
    add_meme.create_meme("", payload, headers)
    add_meme.check_status_code(401)
