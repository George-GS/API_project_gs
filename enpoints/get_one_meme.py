import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetOneMeme(BaseEndpoint):
    '''Класс для получения одного мема по id'''

    @allure.step('Получение мема по id')
    def get_meme_by_id(self, id_meme, headers):
        self.response = requests.get(f'{self.BASE_URL}/meme/{id_meme}', headers=headers)
        return self.response

    @allure.step('Попытка получения мема через POST запрос (неверный метод)')
    def get_meme_by_id_post_method(self, id_meme, headers):
        self.response = requests.post(f'{self.BASE_URL}/meme/{id_meme}', headers=headers)
        return self.response
