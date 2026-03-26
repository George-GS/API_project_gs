




















import allure
import pytest
import meme_data


@allure.feature('Meme API')
class TestDeleteMeme:

    # ==================== ПОЗИТИВНЫЕ ТЕСТЫ ====================

    @allure.story('Удаление мема')
    @allure.title('Удаление существующего мема')
    def test_delete_meme_success(self, delete_meme_endpoint, create_meme_and_get_id, api_headers):
        id_meme = create_meme_and_get_id
        delete_meme_endpoint.delete_meme(id_meme, api_headers)
        delete_meme_endpoint.check_status_code(200)

    @allure.story('Удаление мема')
    @allure.title('Проверка, что после удаления мем недоступен')
    def test_delete_meme_and_verify_not_found(self, delete_meme_endpoint, get_one_meme_endpoint, create_meme_and_get_id, api_headers):
        id_meme = create_meme_and_get_id

        # Удаляем мем
        delete_meme_endpoint.delete_meme(id_meme, api_headers)
        delete_meme_endpoint.check_status_code(200)

        # Пытаемся получить удалённый мем
        get_one_meme_endpoint.get_meme_by_id(api_headers, id_meme)
        get_one_meme_endpoint.check_status_code(404)

    @allure.story('Удаление мема')
    @allure.title('Повторное удаление уже удалённого мема')
    def test_delete_meme_twice(self, delete_meme_endpoint, create_meme_and_get_id, api_headers):
        id_meme = create_meme_and_get_id

        # Первое удаление
        delete_meme_endpoint.delete_meme(id_meme, api_headers)
        delete_meme_endpoint.check_status_code(200)

        # Второе удаление (должно вернуть 404)
        delete_meme_endpoint.delete_meme(id_meme, api_headers)
        delete_meme_endpoint.check_status_code(404)

    # ==================== НЕГАТИВНЫЕ ТЕСТЫ (ID) ====================

    @allure.story('Валидация')
    @allure.title('Удаление мема с несуществующим id')
    def test_delete_meme_not_found(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme(999999999, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.story('Валидация')
    @allure.title('Удаление мема с id = 0')
    def test_delete_meme_id_zero(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme(0, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.story('Валидация')
    @allure.title('Удаление мема с отрицательным id')
    def test_delete_meme_negative_id(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme(-1, api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.story('Валидация')
    @allure.title('Удаление мема с пустым id')
    def test_delete_meme_empty_id(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme('', api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.story('Валидация')
    @allure.title('Удаление мема со строковым id')
    def test_delete_meme_string_id(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme('abc', api_headers)
        delete_meme_endpoint.check_status_code(404)

    # ==================== АВТОРИЗАЦИЯ ====================

    @allure.story('Авторизация')
    @allure.title('Удаление мема без токена')
    def test_delete_meme_unauthorized(self, delete_meme_endpoint, create_meme_and_get_id):
        id_meme = create_meme_and_get_id
        delete_meme_endpoint.delete_meme(id_meme, {})
        delete_meme_endpoint.check_status_code(401)

    @allure.story('Авторизация')
    @allure.title('Удаление мема с невалидным токеном')
    def test_delete_meme_invalid_token(self, delete_meme_endpoint, create_meme_and_get_id):
        id_meme = create_meme_and_get_id
        headers = {'Authorization': 'Bearer invalid_token_12345'}
        delete_meme_endpoint.delete_meme(id_meme, headers)
        delete_meme_endpoint.check_status_code(401)

    @allure.story('Авторизация')
    @allure.title('Удаление мема с пустым токеном')
    def test_delete_meme_empty_token(self, delete_meme_endpoint, create_meme_and_get_id):
        id_meme = create_meme_and_get_id
        headers = {'Authorization': 'Bearer '}
        delete_meme_endpoint.delete_meme(id_meme, headers)
        delete_meme_endpoint.check_status_code(401)

    # ==================== ПРАВА ДОСТУПА ====================

    @allure.story('Права доступа')
    @allure.title('Удаление мема, созданного другим пользователем')
    def test_delete_meme_created_by_other_user(self, delete_meme_endpoint, api_headers_other_user, create_meme_and_get_id):
        id_meme = create_meme_and_get_id
        delete_meme_endpoint.delete_meme(id_meme, api_headers_other_user)
        # Ожидаем 403 (Forbidden) или 404
        delete_meme_endpoint.check_status_code(403)

    # ==================== НЕКОРРЕКТНЫЕ МЕТОДЫ ====================

    @allure.story('Некорректные методы')
    @allure.title('Удаление мема через GET метод')
    def test_delete_meme_with_get_method(self, get_one_meme_endpoint, create_meme_and_get_id, api_headers):
        id_meme = create_meme_and_get_id
        get_one_meme_endpoint.get_meme_by_id(api_headers, id_meme)
        # Ожидаем 405 (Method Not Allowed)
        get_one_meme_endpoint.check_status_code(405)

    @allure.story('Некорректные методы')
    @allure.title('Удаление мема через POST метод')
    def test_delete_meme_with_post_method(self, post_meme_endpoint, create_meme_and_get_id, api_headers):
        id_meme = create_meme_and_get_id
        post_meme_endpoint.post_meme({'some': 'data'}, api_headers)
        # Ожидаем 405
        post_meme_endpoint.check_status_code(405)

    # ==================== БЕЗОПАСНОСТЬ ====================

    @allure.story('Безопасность')
    @allure.title('Удаление мема с SQL инъекцией в id')
    def test_delete_meme_sql_injection(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme("' OR '1'='1", api_headers)
        delete_meme_endpoint.check_status_code(404)

    @allure.story('Безопасность')
    @allure.title('Удаление мема с XSS в id')
    def test_delete_meme_xss_injection(self, delete_meme_endpoint, api_headers):
        delete_meme_endpoint.delete_meme("<script>alert(1)</script>", api_headers)
        delete_meme_endpoint.check_status_code(404)