import pytest
import allure


@allure.feature('')
@allure.story('')
@allure.title('')
def test_authorize(authorize):
    authorize.authorize({'name': 'raman'})
