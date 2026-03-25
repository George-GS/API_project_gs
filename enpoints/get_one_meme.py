import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetOneMeme(BaseEndpoint):
    """

    """

    @allure.step('Получение метода по id')
    def get_meme_by_id(self, headers, id_meme):
        self.response = requests.get(f'{self.BASE_URL}/meme/{id_meme}', headers=headers)
        return self.response

    @allure.step('Получение метода по id')
    def get_meme_by_id_post_method(self, headers, id_meme):
        self.response = requests.post(f'{self.BASE_URL}/meme/{id_meme}', headers=headers)
        return self.response

