import allure
import pytest

import meme_data


class TestPostMeme:
    '''Класс для тестов эндпоинта создания мема'''

    @allure.title('Создание мема с валидными данными')
    @pytest.mark.smoke
    def test_post_meme_with_valid_data(self, post_meme_endpoint, delete_meme_endpoint, api_headers):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, api_headers)
        post_meme_endpoint.check_status_code(200)
        post_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)
        delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme, api_headers)

    @allure.title('Создание мема с разным порядком полей')
    @pytest.mark.regress
    def test_post_meme_different_order(self, post_meme_endpoint, delete_meme_endpoint, api_headers):
        post_meme_endpoint.post_meme(meme_data.body_post_different_order, api_headers)
        post_meme_endpoint.check_status_code(200)
        post_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)
        delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme, api_headers)

    @allure.title('Создание мема с пустым массивом тегов')
    @pytest.mark.regress
    def test_post_meme_empty_tags(self, post_meme_endpoint, delete_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['tags'] = []
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)
        post_meme_endpoint.check_body_response(body)
        delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme, api_headers)

    @allure.title('Создание мема с пустым объектом info')
    @pytest.mark.regress
    def test_post_meme_empty_info(self, post_meme_endpoint, delete_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['info'] = {}
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)
        post_meme_endpoint.check_body_response(body)
        delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme, api_headers)

    @allure.title('Создание мема с пустым телом запроса')
    @pytest.mark.regress
    def test_post_meme_empty_body(self, post_meme_endpoint, api_headers):
        body = {}
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема без поля text')
    @pytest.mark.regress
    def test_post_meme_without_text(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['text']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема без поля url')
    @pytest.mark.regress
    def test_post_meme_without_url(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['url']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема без поля tags')
    @pytest.mark.regress
    def test_post_meme_without_tags(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['tags']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема без поля info')
    @pytest.mark.regress
    def test_post_meme_missing_info(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['info']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с пустым text')
    @pytest.mark.regress
    def test_post_meme_empty_text(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['text'] = ''
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с пустым url')
    @pytest.mark.regress
    def test_post_meme_empty_url(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['url'] = ''
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с tags не массивом, а строкой')
    @pytest.mark.regress
    def test_post_meme_tags_not_array(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['tags'] = 'fun'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с colors не массивом')
    @pytest.mark.regress
    def test_post_meme_colors_not_array(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['info']['colors'] = 'green'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с text не строкой')
    @pytest.mark.regress
    def test_post_meme_text_not_string(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['text'] = 12345
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема без токена')
    @pytest.mark.regress
    def test_post_meme_unauthorized(self, post_meme_endpoint):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, meme_data.headers_no_token)
        post_meme_endpoint.check_status_code(401)

    @allure.title('Создание мема с невалидным токеном')
    @pytest.mark.regress
    def test_post_meme_with_bad_token(self, post_meme_endpoint):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, meme_data.headers_bad_token)
        post_meme_endpoint.check_status_code(401)

    @allure.title('Создание мема с пустым токеном')
    @pytest.mark.regress
    def test_post_meme_with_empty_token(self, post_meme_endpoint):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, meme_data.headers_empty_token)
        post_meme_endpoint.check_status_code(401)

    @allure.title('Создание мема через GET метод')
    @pytest.mark.regress
    def test_post_meme_wrong_method(self, post_meme_endpoint, api_headers):
        post_meme_endpoint.create_meme_get(meme_data.valid_body_for_post_meme, api_headers)
        post_meme_endpoint.check_status_code(405)
