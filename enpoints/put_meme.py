import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class PutMeme(BaseEndpoint):
    '''Класс для работы с эндпоинтом обновления мема'''

    @allure.step('Отправка запроса на полное измененние объекта мема')
    def put_meme(self, id_meme, body, headers):
        self.response = requests.put(f'{self.BASE_URL}/meme/{id_meme}', json=body, headers=headers)
        return self.response

    @allure.step('Попытка полного изменнения мема через POST запрос (неверный метод)')
    def put_meme_with_post_method(self, id_meme, body, headers):
        self.response = requests.post(f'{self.BASE_URL}/meme/{id_meme}', json=body, headers=headers)
        return self.response

    @allure.step('Попытка полного изменения мема через GET запрос')
    def put_meme_with_get_method(self, id_meme, body, headers):
        self.response = requests.get(f'{self.BASE_URL}/meme/{id_meme}', json=body, headers=headers)
        return self.response
