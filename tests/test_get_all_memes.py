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

    @allure.title('Попытка получения всех мемов с невалидной авторизацией: {test_name}')
    @pytest.mark.regress
    @pytest.mark.parametrize('headers, test_name', [
        (meme_data.headers_no_token, 'no_token'),
        (meme_data.headers_bad_token, 'bad_token'),
        (meme_data.headers_empty_token, 'empty_token'),
    ])
    def test_get_all_memes_invalid_auth(self, get_all_memes_endpoint, headers, test_name):
        get_all_memes_endpoint.get_all_memes(headers)
        get_all_memes_endpoint.check_status_code(401)

    @allure.title('Получение списка мемов через POST метод')
    @pytest.mark.regress
    def test_get_all_memes_wrong_method(self, get_all_memes_endpoint, api_headers):
        get_all_memes_endpoint.get_all_memes_post_method(api_headers)
        get_all_memes_endpoint.check_status_code(405)
