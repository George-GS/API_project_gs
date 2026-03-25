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
        self.headers = None

    @allure.step('Проверяем, что статус код 200')
    def check_status_code_200(self):
        assert self.response.status_code == 200
