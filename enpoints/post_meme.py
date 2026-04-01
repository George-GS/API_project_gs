import requests
import allure

import meme_data
from enpoints.base_endpoint import BaseEndpoint


class PostMeme(BaseEndpoint):
    '''Класс для работы с эндпоинтом создания мема'''

    @allure.step('Отправка запроса на создание мема')
    def post_meme(self, body, headers):
        self.response = requests.post(f'{self.BASE_URL}/meme', json=body, headers=headers)
        if self.response.status_code != 200:
            return None
        self.id_meme = self.response.json()['id']
        return self.response

    @allure.step('Попытка создания мема через GET запрос (неверный метод)')
    def create_meme_get(self, body, headers):
        self.response = requests.get(f'{self.BASE_URL}/meme', json=body, headers=headers)
        return self.response
