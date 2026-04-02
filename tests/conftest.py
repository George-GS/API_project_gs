import pytest
from dotenv import load_dotenv, set_key
import os
import random
import string

import meme_data
from enpoints.post_authorize import PostAuthorize
from enpoints.get_authorize_token import GetAuthorizeToken
from enpoints.get_all_memes import GetAllMemes
from enpoints.get_one_meme import GetOneMeme
from enpoints.post_meme import PostMeme
from enpoints.put_meme import PutMeme
from enpoints.delete_meme import DeleteMeme


@pytest.fixture()
def post_authorize_endpoint():
    '''Возвращает экземпляр класса PostAuthorize'''
    return PostAuthorize()


@pytest.fixture()
def get_authorize_token_endpoint():
    '''Возвращает экземпляр класса GetAuthorizeToken'''
    return GetAuthorizeToken()


@pytest.fixture()
def get_all_memes_endpoint():
    '''Возвращает экземпляр класса GetAllMemes'''
    return GetAllMemes()


@pytest.fixture()
def get_one_meme_endpoint():
    '''Возвращает экземпляр класса GetOneMeme'''
    return GetOneMeme()


@pytest.fixture()
def post_meme_endpoint():
    '''Возвращает экземпляр класса PostMeme'''
    return PostMeme()


@pytest.fixture()
def put_meme_endpoint():
    '''Возвращает экземпляр класса PutMeme'''
    return PutMeme()


@pytest.fixture()
def delete_meme_endpoint():
    '''Возвращает экземпляр класса DeleteMeme'''
    return DeleteMeme()


load_dotenv()
token = os.getenv('TOKEN')
token_other_user = os.getenv('TOKEN_OTHER_USER')


@pytest.fixture()
def check_and_get_token(get_authorize_token_endpoint, post_authorize_endpoint):
    '''Проверяет жив ли токен, если нет - получает новый токен, возвращает живой токен'''
    if get_authorize_token_endpoint.check_token(token).status_code == 200:
        return token
    else:
        new_token = post_authorize_endpoint.get_token(meme_data.valid_body_for_post_token)
        set_key('.env', 'TOKEN', new_token)
        return new_token


@pytest.fixture()
def api_headers(check_and_get_token):
    '''Возвращает хэдеры с живым токеном'''
    headers = {'Authorization': f'{check_and_get_token}'}
    return headers


@pytest.fixture()
def check_and_get_token_other_user(get_authorize_token_endpoint, post_authorize_endpoint):
    '''Проверяет жив ли токен, если нет - получает новый токен, возвращает живой токен'''
    if get_authorize_token_endpoint.check_token(token_other_user).status_code == 200:
        return token_other_user
    else:
        new_token = post_authorize_endpoint.get_token(meme_data.valid_body_for_post_token)
        set_key('.env', 'TOKEN_OTHER_USER', new_token)
        return new_token


@pytest.fixture()
def api_headers_other_user(check_and_get_token_other_user):
    '''Возвращает хэдеры с живым токеном ля другого пользователя'''
    headers = {'Authorization': f'{check_and_get_token_other_user}'}
    return headers


@pytest.fixture()
def id_new_meme(post_meme_endpoint, delete_meme_endpoint, api_headers):
    '''Создает новый мем, возвращает его id, после теста удаляем этот мем'''
    post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, api_headers)
    yield post_meme_endpoint.id_meme
    delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme, api_headers)


@pytest.fixture()
def only_create_new_meme(post_meme_endpoint, api_headers):
    '''Создает новый мем, возвращает его id, после теста не удаляем этот мем'''
    post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, api_headers)
    yield post_meme_endpoint.id_meme


@pytest.fixture()
def random_name():
    """Генерирует случайное имя для авторизации"""
    return ''.join(random.choices(string.ascii_lowercase, k=10))


@pytest.fixture
def dynamic_api_headers(post_authorize_endpoint, random_name):
    """Создаёт нового пользователя и возвращает заголовки с его токеном"""
    body = {'name': random_name}
    post_authorize_endpoint.get_token(body)
    token = post_authorize_endpoint.token
    return {'Authorization': token}
