import allure
import pytest


class TestPostAuthorize:
    '''Класс для тестов эндпоинта авторизации'''

    @allure.title("Успешная авторизация с валидным данными")
    @pytest.mark.smoke
    def test_success_auth_with_valid_data(self, post_authorize_endpoint):
        body = {'name': 'george_gs'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(200)
        post_authorize_endpoint.check_response_with_token()

    @allure.title("Повторная авторизация с тем же name")
    @pytest.mark.regress
    def test_repeat_auth_same_name(self, post_authorize_endpoint):
        body = {'name': 'george_gs'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(200)
        post_authorize_endpoint.check_response_with_token()

    @allure.title("Авторизация с длинным name")
    @pytest.mark.regress
    def test_auth_with_long_name(self, post_authorize_endpoint):
        body = {'name': 'name name name name name name name name name name name name'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(200)

    @allure.title("Авторизация с пустым телом")
    @pytest.mark.regress
    def test_auth_with_empty_body(self, post_authorize_endpoint):
        body = {}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)

    @allure.title("Авторизация без поля name")
    @pytest.mark.regress
    def test_auth_without_name_field(self, post_authorize_endpoint):
        body = {'key': 'value'}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)

    @allure.title("Авторизация с разными невалидными именами")
    @pytest.mark.regress
    @pytest.mark.parametrize('name', ['', '   ', '!@#$%^&*()', None])
    def test_auth_with_invalid_names(self, post_authorize_endpoint, name):
        body = {'name': name}
        post_authorize_endpoint.get_token(body)
        post_authorize_endpoint.check_status_code(400)
