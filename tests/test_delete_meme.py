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

    @allure.title('Попытка удаления мема с невалидным id')
    @pytest.mark.regress
    @pytest.mark.parametrize('invalid_id', [999999999, 0, -1, '', 'ид', None])
    def test_delete_meme_invalid_id(self, delete_meme_endpoint, api_headers, invalid_id):
        delete_meme_endpoint.delete_meme(invalid_id, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.title('Попытка удаления мема с невалидной авторизацией: {test_name}')
    @pytest.mark.regress
    @pytest.mark.parametrize('headers, test_name', [
        (meme_data.headers_no_token, 'no_token'),
        (meme_data.headers_bad_token, 'bad_token'),
        (meme_data.headers_empty_token, 'empty_token'),
    ])
    def test_delete_meme_invalid_auth(self, delete_meme_endpoint, id_new_meme, headers, test_name):
        delete_meme_endpoint.delete_meme(id_new_meme, headers)
        delete_meme_endpoint.check_status_code(401)

    @allure.title('Удаление мема, созданного другим пользователем')
    @pytest.mark.regress
    def test_delete_meme_created_by_other_user(self, delete_meme_endpoint, get_one_meme_endpoint, id_new_meme,
                                               api_headers, api_headers_other_user):
        delete_meme_endpoint.delete_meme(id_new_meme, api_headers_other_user)
        delete_meme_endpoint.check_status_code(403)
        get_one_meme_endpoint.get_meme_by_id(id_new_meme, api_headers)
        get_one_meme_endpoint.check_status_code(200)
