import allure
import pytest


class TestPostAuthorize:

    @allure.title("Успешная авторизация с валидным данными")
    def test_success_auth_with_valid_data(self, post_authorize_endpoint):
        body = {'name': 'george_gs'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(200)
        post_authorize_endpoint.check_response_with_token()

    @allure.title("Повторная авторизация с тем же name")
    def test_repeat_auth_same_name(self, post_authorize_endpoint):
        body = {'name': 'george_gs'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(200)
        post_authorize_endpoint.check_response_with_token()

    @allure.title("Авторизация с длинным name")
    def test_auth_with_long_name(self, post_authorize_endpoint):
        body = {'name': 'name name name name name name name name name name name name'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)

    @allure.title("Авторизация с пустым телом")
    def test_auth_with_empty_body(self, post_authorize_endpoint):
        body = {}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)

    @allure.title("Авторизация без поля name")
    def test_auth_without_name_field(self, post_authorize_endpoint):
        body = {'key': 'value'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)

    @allure.title("Авторизация с пустым name")
    def test_auth_with_empty_name(self, post_authorize_endpoint):
        body = {'name': ''}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)

    @allure.title("Авторизация с name в котором только пробелы")
    def test_auth_with_name_only_spaces(self, post_authorize_endpoint):
        body = {'name': '   '}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)
