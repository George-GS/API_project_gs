import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class PostAuthorize(BaseEndpoint):
    '''Класс для работы с эндпоинтом авторизации (получения токена)'''

    def __init__(self):
        super().__init__()
        self.token = None

    @allure.step('Авторизуемся и получаем токен')
    def get_token(self, body):
        self.response = requests.post(f'{self.BASE_URL}/authorize', json=body)
        if self.response.status_code != 200:
            return None
        self.token = self.response.json()['token']
        return self.token

    @allure.step('Проверка наличия и типа токена')
    def check_response_with_token(self):
        assert 'token' in self.response.json(), "Поле 'token' отсутствует"
        token = self.response.json()['token']
        assert isinstance(token, str), f"Токен должен быть строкой, получен {type(token)}"
        assert token, "Токен пустой или None"
