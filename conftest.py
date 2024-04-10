import pytest
import os
import dotenv
from endpoints.authorize import Authorize
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_meme import GetAllMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.token_is_live import TokenIsLive
from endpoints.update_meme import UpdateMeme


@pytest.fixture()
def authorize():
    return Authorize()


@pytest.fixture()
def create_meme():
    return CreateMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def get_all_meme():
    return GetAllMeme()


@pytest.fixture()
def get_meme_by_id():
    return GetMemeById()


@pytest.fixture()
def token_is_live():
    return TokenIsLive()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def get_token(authorize, token_is_live):
    dotenv.load_dotenv()
    token = os.getenv('TOKEN')
    user = os.getenv('USER')

    if token:
        token_is_live.check_token(token)
        if token_is_live.check_status_code(200):
            return token

    authorize.authorize(user)
    token = authorize.token

    return token
