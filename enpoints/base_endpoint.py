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

    def check_status_code(self, status_code):
        with allure.step(f'Проверяем, что статус код = {status_code}'):
            assert self.response.status_code == status_code

    @allure.step('')
    def check_body_response(self, body_response):
        assert self.response.json() == body_response

