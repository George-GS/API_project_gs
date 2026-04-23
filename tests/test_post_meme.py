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

    @allure.title('Создание мема с измененным порядком полей')
    @pytest.mark.regress
    def test_post_meme_different_order(self, post_meme_endpoint, delete_meme_endpoint, api_headers):
        post_meme_endpoint.post_meme(meme_data.body_post_different_order, api_headers)
        post_meme_endpoint.check_status_code(200)
        post_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)
        delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme, api_headers)

    @allure.title('Создание мема с пустым начением поля {field}')
    @pytest.mark.regress
    @pytest.mark.parametrize('field, value', [
        ('tags', []),
        ('info', {}),
        ('text', ''),
        ('url', '')
    ])
    def test_post_meme_empty_values(self, post_meme_endpoint, delete_meme_endpoint, api_headers, field, value):
        body = meme_data.valid_body_for_post_meme.copy()
        body[field] = value
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

    @allure.title('Создание мема без обязательного поля {deleted_field}')
    @pytest.mark.regress
    @pytest.mark.parametrize('deleted_field', ['text', 'url', 'tags', 'info'])
    def test_post_meme_without_required_field(self, post_meme_endpoint, api_headers, deleted_field):
        body = meme_data.valid_body_for_post_meme.copy()
        del body[deleted_field]
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с неверным типом поля: {field}')
    @pytest.mark.regress
    @pytest.mark.parametrize('field, invalid_value', [
        ('text', 12345),
        ('url', 12345),
        ('tags', 'not_array'),
        ('info', 'not_dict'),
    ])
    def test_post_meme_invalid_field_type(self, post_meme_endpoint, api_headers, field, invalid_value):
        body = meme_data.valid_body_for_post_meme.copy()
        body[field] = invalid_value
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с colors не массивом')
    @pytest.mark.regress
    def test_post_meme_colors_not_array(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['info']['colors'] = 'green'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.title('Создание мема с невалидной авторизацией: {test_name}')
    @pytest.mark.regress
    @pytest.mark.parametrize('headers, test_name', [
        (meme_data.headers_no_token, 'no_token'),
        (meme_data.headers_bad_token, 'bad_token'),
        (meme_data.headers_empty_token, 'empty_token'),
    ])
    def test_post_meme_unauthorized_cases(self, post_meme_endpoint, headers, test_name):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, headers)
        post_meme_endpoint.check_status_code(401)

    @allure.title('Создание мема через GET метод')
    @pytest.mark.regress
    def test_post_meme_wrong_method(self, post_meme_endpoint, api_headers):
        post_meme_endpoint.create_meme_get(meme_data.valid_body_for_post_meme, api_headers)
        post_meme_endpoint.check_status_code(405)
