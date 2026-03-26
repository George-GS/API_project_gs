import allure

import meme_data


class TestGetOneMeme:

    @allure.title('Получение одного мема с автоизацией (позитивный кейс)')
    def test_get_one_meme_positive(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(api_headers, 1)
        get_one_meme_endpoint.check_status_code(200)
        get_one_meme_endpoint.check_body_response(meme_data.body_meme_id_1)

    @allure.title('Получение нового созданного мема')
    def test_get_one_meme_new(self, get_one_meme_endpoint, id_new_meme, api_headers):
        get_one_meme_endpoint.get_meme_by_id(api_headers, id_new_meme)
        get_one_meme_endpoint.check_status_code(200)
        get_one_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)

    @allure.title('Получение мема с несуществующим id')
    def test_get_one_meme_id_not_found(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(api_headers, 986796921321)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с id = 0')
    def test_get_one_meme_id_zero(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(api_headers, 0)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с отрицательным id')
    def test_get_one_meme_negative_id(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(api_headers, -1)
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с пустым id')
    def test_get_one_meme_empty_id(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(api_headers, '')
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение мема с строковым id')
    def test_get_one_meme_string_id(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id(api_headers, 'ид')
        get_one_meme_endpoint.check_status_code(404)

    @allure.title('Получение одного мема без авторизации')
    def test_get_meme_by_id_unauthorized(self, get_one_meme_endpoint):
        get_one_meme_endpoint.get_meme_by_id(meme_data.headers_no_token, 1)
        get_one_meme_endpoint.check_status_code(401)

    @allure.title('Получение одного мема c невалидным токеном')
    def test_get_meme_by_id_with_bad_token(self, get_one_meme_endpoint):
        get_one_meme_endpoint.get_meme_by_id(meme_data.headers_bad_token, 1)
        get_one_meme_endpoint.check_status_code(401)

    @allure.title('Получение одного мема c пустым токеном')
    def test_get_meme_by_id_with_empty_token(self, get_one_meme_endpoint):
        get_one_meme_endpoint.get_meme_by_id(meme_data.headers_empty_token, 1)
        get_one_meme_endpoint.check_status_code(401)

    @allure.title('Получение одного мема через POST метод')
    def test_get_meme_by_id_wrong_method(self, get_one_meme_endpoint, api_headers):
        get_one_meme_endpoint.get_meme_by_id_post_method(api_headers, 1)
        get_one_meme_endpoint.check_status_code(405)
