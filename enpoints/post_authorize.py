import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class PostAuthorize(BaseEndpoint):

    @allure.step('Авторизуемся и получаем токен')
    def user_authorization(self, body):
        '''
        Выполняет авторизацию пользователя и возвращает токен доступа.
        :param body: dict - имя пользователя
        :return: str - токен авторизации
        '''
        self.response = requests.post(f'{self.BASE_URL}/authorize', json=body)
        self.token = self.response.json()['token']
        return self.response.json()['token']