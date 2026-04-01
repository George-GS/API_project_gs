import allure
import pytest

import meme_data

class TestDeleteMeme:
    '''Класс для тестов эндпоинта удаления мема'''

    @allure.title('Удаление существующего мема по id, проверка недоступности мема после удаления')
    @pytest.mark.smoke
    def test_delete_meme_with_valid_id(self, delete_meme_endpoint, get_one_meme_endpoint, only_create_new_meme, api_headers):
        delete_meme_endpoint.delete_meme(only_create_new_meme, api_headers)
        delete_meme_endpoint.check_status_code(200)
        delete_meme_endpoint.check_response_text(f'Meme with id {only_create_new_meme} successfully deleted')

        get_one_meme_endpoint.get_meme_by_id(only_create_new_meme, api_headers)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Повторное удаление уже удалённого мема')
    @pytest.mark.regress
    def test_delete_meme_twice(self, delete_meme_endpoint, only_create_new_meme, api_headers):
        delete_meme_endpoint.delete_meme(only_create_new_meme, api_headers)
        delete_meme_endpoint.check_status_code(200)

        delete_meme_endpoint.delete_meme(only_create_new_meme, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.title('Удаление мема с несуществующим id')
    @pytest.mark.regress
    def test_delete_meme_not_found(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme(999999999, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.title('Удаление мема с id = 0')
    @pytest.mark.regress
    def test_delete_meme_id_zero(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme(0, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.title('Удаление мема с отрицательным id')
    @pytest.mark.regress
    def test_delete_meme_negative_id(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme(-1, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.title('Удаление мема с пустым id')
    @pytest.mark.regress
    def test_delete_meme_empty_id(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme('', api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.title('Удаление мема со строковым id')
    @pytest.mark.regress
    def test_delete_meme_string_id(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme('abc', api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.title('Удаление мема без токена')
    @pytest.mark.regress
    def test_delete_meme_unauthorized(self, delete_meme_endpoint, id_new_meme):
        delete_meme_endpoint.delete_meme(id_new_meme, meme_data.headers_no_token)
        delete_meme_endpoint.check_status_code(401)

    @allure.title('Удаление мема с невалидным токеном')
    @pytest.mark.regress
    def test_delete_meme_invalid_token(self, delete_meme_endpoint, id_new_meme):
        delete_meme_endpoint.delete_meme(id_new_meme, meme_data.headers_bad_token)
        delete_meme_endpoint.check_status_code(401)

    @allure.title('Удаление мема с пустым токеном')
    @pytest.mark.regress
    def test_delete_meme_empty_token(self, delete_meme_endpoint, id_new_meme):
        delete_meme_endpoint.delete_meme(id_new_meme, meme_data.headers_empty_token)
        delete_meme_endpoint.check_status_code(401)

    @allure.title('Удаление мема, созданного другим пользователем')
    @pytest.mark.regress
    def test_delete_meme_created_by_other_user(self, delete_meme_endpoint, get_one_meme_endpoint, id_new_meme,
                                               api_headers, api_headers_other_user):
        delete_meme_endpoint.delete_meme(id_new_meme, api_headers_other_user)
        delete_meme_endpoint.check_status_code(403)
        get_one_meme_endpoint.get_meme_by_id(id_new_meme, api_headers)
        get_one_meme_endpoint.check_status_code(200)
