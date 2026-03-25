import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetAuthorizeToken(BaseEndpoint):

    @allure.step('Проверяем активен ли токен')
    def check_token(self, token):
        self.response = requests.get(f'{self.BASE_URL}/authorize/{token}')
        return self.response.text
