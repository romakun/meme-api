import pytest
import allure


@allure.feature('Meme CRUD')
@allure.story('Get')
@pytest.mark.smoke
@allure.title('Получение мема по id')
def test_get_meme_by_id(get_active_token, get_meme, new_meme):
    get_meme.get_meme_by_id(get_active_token, new_meme.meme_id)
    get_meme.check_status_code(200)
    get_meme.check_response_body(new_meme.json)


@allure.feature('Meme CRUD')
@allure.story('Get')
@pytest.mark.regression
@allure.title('Получение мема другого пользователя')
def test_get_meme_of_another_user(get_active_token, get_meme, auth, new_meme):
    another_user = {'name': 'another_user'}
    auth.authorize(another_user)
    another_user_token = auth.token
    get_meme.get_meme_by_id(another_user_token, new_meme.meme_id)
    get_meme.check_status_code(200)


@allure.feature('Meme CRUD')
@allure.story('Get')
@pytest.mark.regression
@allure.title('Получение мема по несуществующему id')
def test_get_meme_by_wrong_id(get_active_token, get_meme):
    get_meme.get_meme_by_id(get_active_token, "wrong_id")
    get_meme.check_status_code(404)


@allure.feature('Meme CRUD')
@allure.story('Get')
@pytest.mark.regression
@allure.title('Получение мема по id без токена')
@pytest.mark.parametrize('headers', [
    {'Content-type': 'application/json', 'Authorization': 'wrong_token'},
    {'Content-type': 'application/json', 'Authorization': ''},
    {'Content-type': 'application/json'}
])
def test_get_meme_without_token(get_meme, new_meme, headers):
    get_meme.get_meme_by_id("", new_meme.meme_id, headers)
    get_meme.check_status_code(401)
