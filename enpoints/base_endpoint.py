import allure


class BaseEndpoint:
    '''
    Базовый класс для всех API-эндпоинтов.
    Содержит общие атрибуты и методы для работы с API.
    '''

    BASE_URL = 'http://memesapi.course.qa-practice.com'

    def __init__(self):
        self.token = None
        self.body = None
        self.response = None
        self.headers = None
        self.id_meme = None

    @allure.step('Проверка статус кода ответа')
    def check_status_code(self, expected_code):
        with allure.step(f'Проверяем, что статус код = {expected_code}'):
            actual_code = self.response.status_code
            assert self.response.status_code == expected_code, \
                f'Ожидался статус код {expected_code}, получен {actual_code}'

    @allure.step('Проверка тела ответа на соответсвие проверяемому')
    def check_body_response(self, expected_body_response):
        actual_body = self.response.json()
        assert 'id' in actual_body, 'В ответе нет id'
        assert actual_body['text'] == expected_body_response['text'], \
            f"text: ожидалось {expected_body_response['text']}, получено {actual_body['text']}"
        assert actual_body['url'] == expected_body_response['url'], \
            f"url: ожидалось {expected_body_response['url']}, получено {actual_body['url']}"
        assert actual_body['tags'] == expected_body_response['tags'], \
            f"tags: ожидалось {expected_body_response['tags']}, получено {actual_body['tags']}"
        assert actual_body['info'] == expected_body_response['info'], \
            f"info: ожидалось {expected_body_response['info']}, получено {actual_body['info']}"

    @allure.step('Проверка текста ответа')
    def check_response_text(self, expected_text):
        assert self.response.text == expected_text, \
            f"Ожидалось: {expected_text}, " \
            f"получено: {self.response.text}"
