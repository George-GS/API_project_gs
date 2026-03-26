import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class PostMeme(BaseEndpoint):
    '''

    '''
    @allure.step('')
    def post_meme(self, body, headers):
        self.response = requests.post(f'{self.BASE_URL}/meme', json=body, headers=headers)
        self.id_meme = self.response.json()['id']
        return self.response


    @allure.step('')
    def









        @allure.step('Проверка, что ответ содержит все отправленные поля')
        def check_response_matches_sent_body(self, sent_body):
            actual = self.response.json()

            # Проверяем, что в ответе есть id
            assert 'id' in actual, "В ответе нет id"

            # Проверяем только отправленные поля
            assert actual['text'] == sent_body[
                'text'], f"text: ожидалось {sent_body['text']}, получено {actual['text']}"
            assert actual['url'] == sent_body['url'], f"url: ожидалось {sent_body['url']}, получено {actual['url']}"
            assert actual['tags'] == sent_body[
                'tags'], f"tags: ожидалось {sent_body['tags']}, получено {actual['tags']}"
            assert actual['info']['colors'] == sent_body['info'][
                'colors'], f"colors: ожидалось {sent_body['info']['colors']}, получено {actual['info']['colors']}"










