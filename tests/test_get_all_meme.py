import pytest
import allure


@allure.feature('Meme CRUD')
@allure.story('Get')
@pytest.mark.smoke
@allure.title('Получение всех мемов')
@pytest.mark.parametrize('several_new_meme', [3], indirect=True)
def test_get_all_meme(get_meme_count, several_new_meme, get_active_token, get_all):
    get_all.get_all_meme(get_active_token)
    get_all.check_status_code(200)
    get_all.check_meme_count(get_meme_count + len(several_new_meme))
    get_all.check_meme_body(several_new_meme[0])


@allure.feature('Meme CRUD')
@allure.story('Get')
@pytest.mark.regression
@allure.title('Получение всех мемов без токена')
@pytest.mark.parametrize('headers', [
    {'Content-type': 'application/json', 'Authorization': 'wrong_token'},
    {'Content-type': 'application/json', 'Authorization': ''},
    {'Content-type': 'application/json'}
])
def test_get_all_meme_without_token(get_all, headers):
    get_all.get_all_meme("", headers)
    get_all.check_status_code(401)
