import pytest
import os
from dotenv import load_dotenv, set_key
from endpoints.authorize import Authorize
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_meme import GetAllMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.token_is_live import TokenIsLive
from endpoints.update_meme import UpdateMeme
from utils.meme_utils import generate_meme_body as random_meme


@pytest.fixture()
def auth():
    return Authorize()


@pytest.fixture()
def add_meme():
    return CreateMeme()


@pytest.fixture()
def remove_meme():
    return DeleteMeme()


@pytest.fixture()
def get_all():
    return GetAllMeme()


@pytest.fixture()
def get_meme():
    return GetMemeById()


@pytest.fixture()
def token_status():
    return TokenIsLive()


@pytest.fixture()
def change_meme():
    return UpdateMeme()


@pytest.fixture()
def get_active_token(auth, token_status):
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv()
    token = os.getenv('TOKEN')
    user = os.getenv('USER')
    payload = {'name': user}

    if token:
        token_status.check_token(token)
        if token_status.isLive:
            return token

    auth.authorize(payload)
    token = auth.token
    set_key(env_path, "TOKEN", token)

    return token


@pytest.fixture()
def new_meme(get_active_token, add_meme, remove_meme):
    payload = random_meme()
    add_meme.create_meme(get_active_token, payload)
    yield add_meme
    remove_meme.delete_meme(get_active_token, add_meme.meme_id)


@pytest.fixture()
def several_new_meme(request, get_active_token, add_meme, remove_meme):
    count = request.param
    new_memes = []
    for _ in range(count):
        payload = random_meme()
        add_meme.create_meme(get_active_token, payload)
        meme = add_meme.json
        new_memes.append(meme)
    yield new_memes
    for meme in new_memes:
        remove_meme.delete_meme(get_active_token, meme['id'])


@pytest.fixture()
def get_meme_count(get_active_token, get_all):
    get_all.get_all_meme(get_active_token)
    return len(get_all.json['data'])
