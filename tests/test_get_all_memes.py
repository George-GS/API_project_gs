import allure
import pytest

import meme_data


class TestGetAllMemes:
    '''Класс для тестов эндпоинта получения всех мемов'''

    @allure.title('Получение всех мемов с автоизацией (позитивный кейс)')
    @pytest.mark.smoke
    def test_get_all_memes_positive(self, get_all_memes_endpoint, api_headers):
        get_all_memes_endpoint.get_all_memes(api_headers)
        get_all_memes_endpoint.check_status_code(200)
        get_all_memes_endpoint.check_body_all_memes()

    @allure.title('Получение всех мемов без авторизации')
    @pytest.mark.regress
    def test_get_all_memes_unauthorized(self, get_all_memes_endpoint):
        get_all_memes_endpoint.get_all_memes(meme_data.headers_no_token)
        get_all_memes_endpoint.check_status_code(401)

    @allure.title('Получение всех мемов c невалидным токеном')
    @pytest.mark.regress
    def test_get_all_memes_with_bad_token(self, get_all_memes_endpoint):
        get_all_memes_endpoint.get_all_memes(meme_data.headers_bad_token)
        get_all_memes_endpoint.check_status_code(401)

    @allure.title('Получение всех мемов c пустым токеном')
    @pytest.mark.regress
    def test_get_all_memes_with_empty_token(self, get_all_memes_endpoint):
        get_all_memes_endpoint.get_all_memes(meme_data.headers_empty_token)
        get_all_memes_endpoint.check_status_code(401)

    @allure.title('Получение списка мемов через POST метод')
    @pytest.mark.regress
    def test_get_all_memes_wrong_method(self, get_all_memes_endpoint, api_headers):
        get_all_memes_endpoint.get_all_memes_post_method(api_headers)
        get_all_memes_endpoint.check_status_code(405)
