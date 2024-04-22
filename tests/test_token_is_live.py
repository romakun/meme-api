import pytest
import allure


@allure.feature('Auth')
@allure.story('token')
@pytest.mark.smoke
@allure.title('Проверка токена')
def test_token_is_live(get_active_token, token_status):
    token_status.check_token(get_active_token)
    token_status.check_status_code(200)
