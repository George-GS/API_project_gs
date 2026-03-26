import pytest
from dotenv import load_dotenv, set_key
import os

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
    '''Возвращает экземляр класса PostAuthorize'''
    return PostAuthorize()


@pytest.fixture()
def get_authorize_token_endpoint():
    '''Возвращает экземляр класса GetAuthorizeToken'''
    return GetAuthorizeToken()


@pytest.fixture()
def get_all_memes_endpoint():
    '''Возвращает экземляр класса GetAllMemes'''
    return GetAllMemes()


@pytest.fixture()
def get_one_meme_endpoint():
    '''Возвращает экземляр класса GetOneMeme'''
    return GetOneMeme()


@pytest.fixture()
def post_meme_endpoint():
    '''Возвращает экземляр класса PostMeme'''
    return PostMeme()


@pytest.fixture()
def put_meme_endpoint():
    '''Возвращает экземляр класса PutMeme'''
    return PutMeme()


@pytest.fixture()
def delete_meme_endpoint():
    '''Возвращает экземляр класса DeleteMeme'''
    return DeleteMeme()


load_dotenv()
token = os.getenv('TOKEN')


@pytest.fixture()
def check_and_get_token(get_authorize_token_endpoint, post_authorize_endpoint):
    """Проверяет жив ли токен, если нет - получает новый токен, возвращает живой токен"""
    if get_authorize_token_endpoint.check_token(token).status_code == 200:
        return token
    else:
        new_token = post_authorize_endpoint.user_authorization(meme_data.valid_body_for_post_token)
        set_key('.env', 'TOKEN', new_token)
        return new_token


@pytest.fixture()
def api_headers(check_and_get_token):
    '''Возвращает хэдеры с живым токеном'''
    headers = {'Authorization': check_and_get_token}
    return headers


@pytest.fixture()
def id_new_meme(post_meme_endpoint, delete_meme_endpoint):
    """Создает новый мем, возвращает его id, после теста удаляем этот мем"""
    post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme)
    yield post_meme_endpoint.id_meme
    delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme)

@pytest.fixture()
def only_create_new_meme(post_meme_endpoint):
    """Создает новый мем, возвращает его id, после теста удаляем этот мем"""
    post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme)
    yield post_meme_endpoint.id_meme



@pytest.fixture()
def put_body(put_meme_endpoint, id_new_meme):
    """Возвращает тело для PUT запроса с созданным ID"""
    body = meme_data.valid_body_for_put_meme.copy()
    body['id'] = id_new_meme
    return body




