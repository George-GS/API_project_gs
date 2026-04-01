import allure
import pytest

import meme_data


class TestPutMeme:
    '''Класс для тестов эндпоинта обновления мема (PUT)'''

    @allure.title('Полное обновление существующего мема с валидными данными')
    @pytest.mark.smoke
    def test_put_meme_with_valid_data(self,  put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(200)
        put_meme_endpoint.check_body_response(body)

    @allure.title('Обновление мема с пустым массивом тегов')
    @pytest.mark.regress
    def test_put_meme_empty_tags(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        body['tags'] = []
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(200)
        put_meme_endpoint.check_body_response(body)

    @allure.title('Обновление мема с разным порядком полей')
    @pytest.mark.regress
    def test_put_meme_different_order(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(200)
        put_meme_endpoint.check_body_response(body)

    @allure.title('Обновление несуществующего мема')
    @pytest.mark.regress
    def test_put_meme_not_found(self, put_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = 999999999
        put_meme_endpoint.put_meme(999999999, meme_data.valid_body_for_put_meme, api_headers)
        put_meme_endpoint.check_status_code(404)

    @allure.title('Обновление мема с id = 0')
    @pytest.mark.regress
    def test_put_meme_id_zero(self, put_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = 0
        put_meme_endpoint.put_meme(0, meme_data.valid_body_for_put_meme, api_headers)
        put_meme_endpoint.check_status_code(404)

    @allure.title('Обновление мема с отрицательным id')
    @pytest.mark.regress
    def test_put_meme_negative_id(self, put_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = -1
        put_meme_endpoint.put_meme(-1, meme_data.valid_body_for_put_meme, api_headers)
        put_meme_endpoint.check_status_code(404)

    @allure.title('Обновление мема с пустым телом')
    @pytest.mark.regress
    def test_put_meme_empty_body(self, put_meme_endpoint, id_new_meme, api_headers):
        put_meme_endpoint.put_meme(id_new_meme, {}, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема без поля text')
    @pytest.mark.regress
    def test_put_meme_missing_text(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        del body['text']
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема без поля url')
    @pytest.mark.regress
    def test_put_meme_missing_url(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        del body['url']
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема без поля tags')
    @pytest.mark.regress
    def test_put_meme_missing_tags(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        del body['tags']
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема без поля info')
    @pytest.mark.regress
    def test_put_meme_missing_info(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        del body['info']
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема с пустым text')
    @pytest.mark.regress
    def test_put_meme_empty_text(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        body['text'] = ''
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(200)

    @allure.title('Обновление мема с пустым url')
    @pytest.mark.regress
    def test_put_meme_empty_url(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        body['url'] = ''
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(200)

    @allure.title('Обновление мема с tags не массивом')
    @pytest.mark.regress
    def test_put_meme_tags_not_array(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        body['tags'] = 'not_array'
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема с colors не массивом')
    @pytest.mark.regress
    def test_put_meme_colors_not_array(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        body['info']['colors'] = 'not_array'
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема без токена')
    @pytest.mark.regress
    def test_put_meme_unauthorized(self, put_meme_endpoint, id_new_meme):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, {})
        put_meme_endpoint.check_status_code(401)

    @allure.title('Обновление мема с невалидным токеном')
    @pytest.mark.regress
    def test_put_meme_invalid_token(self, put_meme_endpoint, id_new_meme):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, meme_data.headers_bad_token)
        put_meme_endpoint.check_status_code(401)

    @allure.title('Обновление мема с пустым токеном')
    @pytest.mark.regress
    def test_put_meme_empty_token(self, put_meme_endpoint, id_new_meme):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, meme_data.headers_empty_token)
        put_meme_endpoint.check_status_code(401)

    @allure.title('Обновление мема, созданного другим пользователем')
    @pytest.mark.regress
    def test_put_meme_created_by_other_user(self, put_meme_endpoint, id_new_meme, api_headers_other_user):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers_other_user)
        put_meme_endpoint.check_status_code(403)

    @allure.title('Обновление мема через GET метод')
    @pytest.mark.regress
    def test_put_meme_with_get_method(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme_with_get_method(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(405)

    @allure.title('Обновление мема через POST метод')
    @pytest.mark.regress
    def test_put_meme_with_post_method(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme_with_post_method(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(405)
