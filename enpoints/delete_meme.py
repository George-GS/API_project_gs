import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    '''Класс для работы с эндпоинтом удаления мема'''

    @allure.step('Удаляем мем по id')
    def delete_meme(self, id_meme, headers):
        self.response = requests.delete(f'{self.BASE_URL}/meme/{id_meme}', headers=headers)
        return self.response
