import pytest
import allure


@allure.feature('Meme CRUD')
@allure.story('Delete')
@pytest.mark.smoke
@allure.title('Удаление мема')
def test_delete_meme(get_active_token, new_meme, remove_meme, get_meme):
    remove_meme.delete_meme(get_active_token, new_meme.meme_id)
    remove_meme.check_status_code(200)
    get_meme.get_meme_by_id(get_active_token, new_meme.meme_id)
    get_meme.check_status_code(404)


@allure.feature('Meme CRUD')
@allure.story('Delete')
@pytest.mark.regression
@allure.title('Удаление мема не создателем')
def test_delete_meme_by_another_user(get_active_token, new_meme, remove_meme, auth):
    payload = {'name': 'another_user'}
    auth.authorize(payload)
    remove_meme.delete_meme(auth.token, new_meme.meme_id)
    remove_meme.check_status_code(403)


@allure.feature('Meme CRUD')
@allure.story('Delete')
@pytest.mark.regression
@allure.title('Удаление мема по несуществующему id')
def test_get_meme_by_wrong_id(get_active_token, remove_meme):
    remove_meme.delete_meme(get_active_token, "wrong_id")
    remove_meme.check_status_code(404)


@allure.feature('Meme CRUD')
@allure.story('Delete')
@pytest.mark.regression
@allure.title('Удаление мема по id без токена')
@pytest.mark.parametrize('headers', [
    {'Content-type': 'application/json', 'Authorization': 'wrong_token'},
    {'Content-type': 'application/json', 'Authorization': ''},
    {'Content-type': 'application/json'}
])
def test_delete_meme_without_token(remove_meme, new_meme, headers):
    remove_meme.delete_meme("", new_meme.meme_id, headers)
    remove_meme.check_status_code(401)
