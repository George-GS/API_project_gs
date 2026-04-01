import allure
import pytest

import meme_data


class TestGetOneMeme:
    '''Класс для тестов эндпоинта получения одного мема'''

    @allure.title('Получение одного мема с автоизацией (позитивный кейс)')
    @pytest.mark.smoke
    def test_get_one_meme_positive(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(1, api_headers)
        get_one_meme_endpoint.check_status_code(200)
        get_one_meme_endpoint.check_body_response(meme_data.body_meme_id_1)

    @allure.title('Получение нового созданного мема')
    @pytest.mark.regress
    def test_get_one_meme_new(self, get_one_meme_endpoint, id_new_meme, api_headers):
        get_one_meme_endpoint.get_meme_by_id(id_new_meme, api_headers)
        get_one_meme_endpoint.check_status_code(200)
        get_one_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)

    @allure.title('Получение мема с несуществующим id')
    @pytest.mark.regress
    def test_get_one_meme_id_not_found(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(986796921321, api_headers)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с id = 0')
    @pytest.mark.regress
    def test_get_one_meme_id_zero(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(0, api_headers)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с отрицательным id')
    @pytest.mark.regress
    def test_get_one_meme_negative_id(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(-1, api_headers)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с пустым id')
    @pytest.mark.regress
    def test_get_one_meme_empty_id(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id('', api_headers)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с строковым id')
    @pytest.mark.regress
    def test_get_one_meme_string_id(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id('ид', api_headers)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение одного мема без авторизации')
    @pytest.mark.regress
    def test_get_meme_by_id_unauthorized(self, get_one_meme_endpoint):
        get_one_meme_endpoint.get_meme_by_id(1, meme_data.headers_no_token)
        get_one_meme_endpoint.check_status_code(401)

    @allure.title('Получение одного мема c невалидным токеном')
    @pytest.mark.regress
    def test_get_meme_by_id_with_bad_token(self, get_one_meme_endpoint):
        get_one_meme_endpoint.get_meme_by_id(1, meme_data.headers_bad_token)
        get_one_meme_endpoint.check_status_code(401)

    @allure.title('Получение одного мема c пустым токеном')
    @pytest.mark.regress
    def test_get_meme_by_id_with_empty_token(self, get_one_meme_endpoint):
        get_one_meme_endpoint.get_meme_by_id(1, meme_data.headers_empty_token)
        get_one_meme_endpoint.check_status_code(401)

    @allure.title('Получение одного мема через POST метод')
    @pytest.mark.regress
    def test_get_meme_by_id_wrong_method(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id_post_method(1, api_headers)
        get_one_meme_endpoint.check_status_code(405)
