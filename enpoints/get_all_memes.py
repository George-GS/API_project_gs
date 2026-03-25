import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetAllMemes(BaseEndpoint):
    '''

    '''
    @allure.step('Получение всех мемов')
    def get_all_memes(self, headers):
        self.response = requests.get(f'{self.BASE_URL}/meme', headers=headers)
        self.json_response = self.response.json()
        return self.response

    @allure.step('Проверяем структуру ответа при получении всех мемов')
    def check_body_all_memes(self):
        assert isinstance(self.json_response, dict)
        assert 'data' in self.json_response

    @allure.step('Отправляем post запрос для получения мема')
    def get_all_memes_post_method(self, headers):
        self.response = requests.post(f'{self.BASE_URL}/meme', headers=headers)
        return self.response
