import requests
import allure


class BaseEndpoint:
    """
    Базовый класс для всех API-эндпоинтов.
    Содержит общие атрибуты и методы для работы с API.
    """

    BASE_URL = 'http://memesapi.course.qa-practice.com'

    def __init__(self):
        self.token = None
        self.body = None
        self.response = None
        self.json_response = None
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
        actual_body_response = self.response.json()
        assert actual_body_response == expected_body_response, \
            f'Ожидался овтет {expected_body_response}' \
            f'Получен овтет {actual_body_response}'

