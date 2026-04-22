import allure
import pytest


class TestCheckToken:
    '''Класс для тестов проверки токена'''

    @allure.title('Проверка существующего активного токена')
    @pytest.mark.smoke
    def test_check_active_token(self, get_authorize_token_endpoint, check_and_get_token):
        get_authorize_token_endpoint.check_token(check_and_get_token)
        get_authorize_token_endpoint.check_status_code(200)
        get_authorize_token_endpoint.check_text_get_token()

    @allure.title('Проверка невалидного токена')
    @pytest.mark.regress
    @pytest.mark.parametrize('token', ['abcd123', '', 654564, '!@#$%^&*()', None])
    def test_check_invalid_token(self, get_authorize_token_endpoint, token):
        get_authorize_token_endpoint.check_token(token)
        get_authorize_token_endpoint.check_status_code(404)

    @allure.title('Проверка токена через POST метод')
    @pytest.mark.regress
    def test_check_token_wrong_method(self, get_authorize_token_endpoint, check_and_get_token):
        get_authorize_token_endpoint.post_check_token(check_and_get_token)
        get_authorize_token_endpoint.check_status_code(405)
