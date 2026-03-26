import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class PostAuthorize(BaseEndpoint):

    @allure.step('Авторизуемся и получаем токен')
    def get_token(self, body):
        '''
        Выполняет авторизацию пользователя и возвращает токен доступа.
        :param body: dict - имя пользователя
        :return: str - токен авторизации
        '''
        self.response = requests.post(f'{self.BASE_URL}/authorize', json=body)
        self.token = self.response.json()['token']
        return self.token

    @allure.step('')
    def check_response_with_token(self):
        assert 'token' in self.response, "Поле 'token' отсутствует"
        token = self.response['token'],
        assert isinstance(token, str), f"Токен должен быть строкой, получен {type(token)}"
        assert token, "Токен пустой или None"