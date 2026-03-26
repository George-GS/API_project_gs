import allure


class TestCheckToken:

    @allure.title('Проверка существующего активного токена')
    def test_check_active_token(self, get_authorize_token_endpoint, check_and_get_token):
        get_authorize_token_endpoint.check_token(check_and_get_token)
        get_authorize_token_endpoint.check_status_code(200)
        get_authorize_token_endpoint.check_text_get_token()

    @allure.title('Проверка активности несуществующего токена')
    def test_check_token_not_exists(self, get_authorize_token_endpoint):
        token = 'abcd123'
        get_authorize_token_endpoint.check_token(token)
        get_authorize_token_endpoint.check_status_code(404)

    @allure.title('Проверка активности пустого токена')
    def test_check_token_empty(self, get_authorize_token_endpoint):
        token = ''
        get_authorize_token_endpoint.check_token(token)
        get_authorize_token_endpoint.check_status_code(405)

    @allure.title('Проверка активности числового токена')
    def test_check_token_numeric(self, get_authorize_token_endpoint):
        token = 654564
        get_authorize_token_endpoint.check_token(token)
        get_authorize_token_endpoint.check_status_code(404)

    @allure.title('Проверка токена со спецсимволами')
    def test_check_token_special_chars(self, get_authorize_token_endpoint):
        token = '!@#$%^&*()'
        get_authorize_token_endpoint.check_token(token)
        get_authorize_token_endpoint.check_status_code(404)

    @allure.title('Проверка токена через POST метод')
    def test_check_token_wrong_method(self, get_authorize_token_endpoint, check_and_get_token):
        get_authorize_token_endpoint.post_check_token(check_and_get_token)
        get_authorize_token_endpoint.check_status_code(405)

    @allure.title('Проверка токена со значением None')
    def test_check_token_none(self, get_authorize_token_endpoint):
        token = None
        get_authorize_token_endpoint.check_token(token)
        get_authorize_token_endpoint.check_status_code(404)



