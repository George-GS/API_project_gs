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

    @allure.title('Обновление мема с разным порядком полей')
    @pytest.mark.regress
    def test_put_meme_different_order(self, put_meme_endpoint, id_new_meme, api_headers):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(200)
        put_meme_endpoint.check_body_response(body)

    @allure.title('Обновление мема c неверным id: {test_name}')
    @pytest.mark.regress
    @pytest.mark.parametrize('id_values, test_name', [
        (999999999, 'non-existent id'),
        (0, 'id = 0'),
        (-1, 'negative id'),
    ])
    def test_put_meme_invalid_id(self, put_meme_endpoint, api_headers, id_values, test_name):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_values
        put_meme_endpoint.put_meme(id_values, body, api_headers)
        put_meme_endpoint.check_status_code(404)

    @allure.title('Обновление мема с пустым телом')
    @pytest.mark.regress
    def test_put_meme_empty_body(self, put_meme_endpoint, id_new_meme, api_headers):
        put_meme_endpoint.put_meme(id_new_meme, {}, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема без обязательного поля {deleted_field}')
    @pytest.mark.regress
    @pytest.mark.parametrize('deleted_field', ['text', 'url', 'tags', 'info'])
    def test_put_meme_without_required_field(self, put_meme_endpoint, id_new_meme, api_headers, deleted_field):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        del body[deleted_field]
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(400)

    @allure.title('Обновление мема с пустыми значениями поля {field}')
    @pytest.mark.regress
    @pytest.mark.parametrize('field, value', [
        ('tags', []),
        ('text', ''),
        ('url', ''),
    ])
    def test_put_meme_empty_values(self, put_meme_endpoint, id_new_meme, api_headers, field, value):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        body[field] = value
        put_meme_endpoint.put_meme(id_new_meme, body, api_headers)
        put_meme_endpoint.check_status_code(200)
        put_meme_endpoint.check_body_response(body)

    @allure.title('Обновление мема с неверным типом поля: {field}')
    @pytest.mark.regress
    @pytest.mark.parametrize('field, invalid_value', [
        ('text', 12345),
        ('url', 12345),
        ('tags', 'not_array'),
        ('info', 'not_dict'),
    ])
    def test_put_meme_invalid_field_type(self, put_meme_endpoint, id_new_meme, api_headers, field, invalid_value):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        body[field] = invalid_value
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

    @allure.title('Обновление мема с невалидной авторизацией: {test_name}')
    @pytest.mark.regress
    @pytest.mark.parametrize('headers, test_name', [
        ({}, 'без токена'),
        (meme_data.headers_bad_token, 'невалидный токен'),
        (meme_data.headers_empty_token, 'пустой токен'),
    ])
    def test_put_meme_unauthorized_cases(self, put_meme_endpoint, id_new_meme, headers, test_name):
        body = meme_data.valid_body_for_put_meme.copy()
        body['id'] = id_new_meme
        put_meme_endpoint.put_meme(id_new_meme, body, headers)
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
