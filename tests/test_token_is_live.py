import pytest
import allure


@allure.feature('')
@allure.story('')
@allure.title('')
def test_token_is_live(authorize, token_is_live):
    authorize.authorize({'name': 'raman'})
    token = authorize.token
    token_is_live.check_token(token)
