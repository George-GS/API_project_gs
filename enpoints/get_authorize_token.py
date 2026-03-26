import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetAuthorizeToken(BaseEndpoint):

    @allure.step('Проверяем активен ли токен')
    def check_token(self, token):
        self.response = requests.get(f'{self.BASE_URL}/authorize/{token}')
        return self.response

    @allure.step('Проверяем текст в ответе')
    def check_text_get_token(self):
        assert self.response.text.startswith('Token is alive.'), 'Текст ответа не содержит "Token is alive."'

    @allure.step('Проверяем активность токена через неверный метод')
    def post_check_token(self, token):
        self.response = requests.post(f'{self.BASE_URL}/authorize/{token}')
        return self.response
