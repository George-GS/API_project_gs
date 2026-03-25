import requests
import allure
import pytest
from dotenv import load_dotenv, set_key
import os

from enpoints.post_authorize import PostAuthorize
from enpoints.get_object import GetObjects
from enpoints.get_authorize_token import GetAuthorizeToken
from enpoints.get_one_object import GetOneObject

load_dotenv()
token = os.getenv('TOKEN')
body = {'name': 'george_gs'}

@pytest.fixture()
def post_authorize_endpoint():
    return PostAuthorize()


@pytest.fixture()
def get_authorize_token_endpoint():
    return GetAuthorizeToken()


@pytest.fixture()
def get_object_endpoint():
    return GetObjects()

@pytest.fixture()
def get_one_object_endpoint():
    return GetOneObject()


@pytest.fixture()
def check_and_get_token(get_authorize_token_endpoint, post_authorize_endpoint):
    if get_authorize_token_endpoint.check_token(token).startswith('Token is alive'):
        return token
    else:
        new_token = post_authorize_endpoint.user_authorization(body)
        set_key('.env', 'TOKEN', new_token)
        return new_token


@pytest.fixture()
def api_headers(check_and_get_token):
    headers = {'Authorization': check_and_get_token}
    return headers
