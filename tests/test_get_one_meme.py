import allure
import pytest

import meme_data


class TestGetOneMeme:
    '''Класс для тестов эндпоинта получения одного мема'''

    @allure.title('Получение нового созданного мема')
    @pytest.mark.regress
    def test_get_one_meme_new(self, get_one_meme_endpoint, id_new_meme, api_headers):
        get_one_meme_endpoint.get_meme_by_id(id_new_meme, api_headers)
        get_one_meme_endpoint.check_status_code(200)
        get_one_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)

    @allure.title('Попытка получения мема с невалидным id: {invalid_id}')
    @pytest.mark.regress
    @pytest.mark.parametrize('invalid_id', [999999999, 0, -1, '', 'ид', None])
    def test_get_one_meme_invalid_id(self, get_one_meme_endpoint, api_headers, invalid_id):
        get_one_meme_endpoint.get_meme_by_id(invalid_id, api_headers)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Попытка получения мема с невалидной авторизацией: {test_name}')
    @pytest.mark.regress
    @pytest.mark.parametrize('headers, test_name', [
        (meme_data.headers_no_token, 'no_token'),
        (meme_data.headers_bad_token, 'bad_token'),
        (meme_data.headers_empty_token, 'empty_token'),
    ])
    def test_get_one_meme_invalid_auth(self, get_one_meme_endpoint, id_new_meme, headers, test_name):
        get_one_meme_endpoint.get_meme_by_id(id_new_meme, headers)
        get_one_meme_endpoint.check_status_code(401)

    @allure.title('Получение одного мема через POST метод')
    @pytest.mark.regress
    def test_get_meme_by_id_wrong_method(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id_post_method(1, api_headers)
        get_one_meme_endpoint.check_status_code(405)
