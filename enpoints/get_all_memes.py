import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetAllMemes(BaseEndpoint):
    '''Класс для работы с эндпоинтом получения всех мемов'''
    @allure.step('Получение всех мемов')
    def get_all_memes(self, headers):
        self.response = requests.get(f'{self.BASE_URL}/meme', headers=headers)
        return self.response

    @allure.step('Проверяем структуру ответа при получении всех мемов')
    def check_body_all_memes(self):
        assert isinstance(self.response.json(), dict)
        assert 'data' in self.response.json()

    @allure.step('Попытка получения всех мемов через POST запрос (неверный метод)')
    def get_all_memes_post_method(self, headers):
        self.response = requests.post(f'{self.BASE_URL}/meme', headers=headers)
        return self.response
