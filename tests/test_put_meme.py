import allure






ФИКСТУРА ДЛЯ ДРУГОГО ПОЛЬЗОВАТЕЛЯ (если нужна):
python
@pytest.fixture()
def api_headers_other_user():
    """Заголовки с токеном другого пользователя"""
    token = get_token_for_user("other_user")  # или другой способ получения
    return {'Authorization': f'Bearer {token}'}

def

    python
    import allure
    import pytest
    import meme_data

    @allure.feature('Meme API')
    class TestPutMeme:

        # ==================== ПОЗИТИВНЫЕ ТЕСТЫ ====================

        @allure.story('Обновление мема')
        @allure.title('Полное обновление существующего мема')
        def test_put_meme_full_update(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = {
                "info": {
                    "colors": ["red", "yellow"]
                },
                "tags": ["new", "updated"],
                "text": "Updated meme text",
                "url": "https://new-url.com/image.jpg"
            }

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(200)
            put_meme_endpoint.check_body_response(new_body)

        @allure.story('Обновление мема')
        @allure.title('Обновление мема с пустым массивом тегов')
        def test_put_meme_empty_tags(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['tags'] = []

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(200)
            put_meme_endpoint.check_response_has_tags([])

        @allure.story('Обновление мема')
        @allure.title('Обновление мема с пустым массивом цветов')
        def test_put_meme_empty_colors(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['info']['colors'] = []

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(200)
            put_meme_endpoint.check_response_has_colors([])

        @allure.story('Обновление мема')
        @allure.title('Обновление мема с одним тегом')
        def test_put_meme_one_tag(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['tags'] = ['only_one']

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(200)

        @allure.story('Обновление мема')
        @allure.title('Обновление мема с одним цветом')
        def test_put_meme_one_color(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['info']['colors'] = ['purple']

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(200)

        @allure.story('Обновление мема')
        @allure.title('Обновление мема с разным порядком полей')
        def test_put_meme_different_order(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = {
                "url": "https://new-order.com/image.jpg",
                "tags": ["order", "test"],
                "text": "Order doesn't matter",
                "info": {
                    "colors": ["black", "white"]
                }
            }

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(200)

        # ==================== НЕГАТИВНЫЕ ТЕСТЫ (НЕСУЩЕСТВУЮЩИЙ МЕМ) ====================

        @allure.story('Валидация')
        @allure.title('Обновление несуществующего мема')
        def test_put_meme_not_found(self, put_meme_endpoint, api_headers):
            new_body = meme_data.valid_body_for_post_meme
            put_meme_endpoint.put_meme(999999999, new_body, api_headers)
            put_meme_endpoint.check_status_code(404)

        @allure.story('Валидация')
        @allure.title('Обновление мема с id = 0')
        def test_put_meme_id_zero(self, put_meme_endpoint, api_headers):
            new_body = meme_data.valid_body_for_post_meme
            put_meme_endpoint.put_meme(0, new_body, api_headers)
            put_meme_endpoint.check_status_code(404)

        @allure.story('Валидация')
        @allure.title('Обновление мема с отрицательным id')
        def test_put_meme_negative_id(self, put_meme_endpoint, api_headers):
            new_body = meme_data.valid_body_for_post_meme
            put_meme_endpoint.put_meme(-1, new_body, api_headers)
            put_meme_endpoint.check_status_code(404)

        # ==================== НЕГАТИВНЫЕ ТЕСТЫ (ОБЯЗАТЕЛЬНЫЕ ПОЛЯ) ====================

        @allure.story('Валидация')
        @allure.title('Обновление мема с пустым телом')
        def test_put_meme_empty_body(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            put_meme_endpoint.put_meme(id_meme, {}, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема без поля text')
        def test_put_meme_missing_text(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            del new_body['text']

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема без поля url')
        def test_put_meme_missing_url(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            del new_body['url']

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема без поля tags')
        def test_put_meme_missing_tags(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            del new_body['tags']

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема без поля info')
        def test_put_meme_missing_info(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            del new_body['info']

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема без поля colors в info')
        def test_put_meme_missing_colors(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['info'] = {}

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        # ==================== НЕГАТИВНЫЕ ТЕСТЫ (НЕПРАВИЛЬНЫЕ ТИПЫ) ====================

        @allure.story('Валидация')
        @allure.title('Обновление мема с пустым text')
        def test_put_meme_empty_text(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['text'] = ''

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема с пустым url')
        def test_put_meme_empty_url(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['url'] = ''

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема с неверным форматом url')
        def test_put_meme_invalid_url(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['url'] = 'not_a_valid_url'

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема с tags не массивом')
        def test_put_meme_tags_not_array(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['tags'] = 'not_array'

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Валидация')
        @allure.title('Обновление мема с colors не массивом')
        def test_put_meme_colors_not_array(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['info']['colors'] = 'not_array'

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        # ==================== ГРАНИЧНЫЕ ЗНАЧЕНИЯ ====================

        @allure.story('Граничные значения')
        @allure.title('Обновление мема с очень длинным text')
        def test_put_meme_long_text(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['text'] = 'a' * 5000

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Граничные значения')
        @allure.title('Обновление мема с очень длинным url')
        def test_put_meme_long_url(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['url'] = 'https://' + 'a' * 5000 + '.com'

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        @allure.story('Граничные значения')
        @allure.title('Обновление мема с множеством тегов')
        def test_put_meme_many_tags(self, put_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme.copy()
            new_body['tags'] = [f'tag_{i}' for i in range(100)]

            put_meme_endpoint.put_meme(id_meme, new_body, api_headers)
            put_meme_endpoint.check_status_code(400)

        # ==================== АВТОРИЗАЦИЯ ====================

        @allure.story('Авторизация')
        @allure.title('Обновление мема без токена')
        def test_put_meme_unauthorized(self, put_meme_endpoint, only_create_new_meme):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme
            put_meme_endpoint.put_meme(id_meme, new_body, {})
            put_meme_endpoint.check_status_code(401)

        @allure.story('Авторизация')
        @allure.title('Обновление мема с невалидным токеном')
        def test_put_meme_invalid_token(self, put_meme_endpoint, only_create_new_meme):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme
            headers = {'Authorization': 'Bearer invalid_token_12345'}
            put_meme_endpoint.put_meme(id_meme, new_body, headers)
            put_meme_endpoint.check_status_code(401)

        @allure.story('Авторизация')
        @allure.title('Обновление мема с пустым токеном')
        def test_put_meme_empty_token(self, put_meme_endpoint, only_create_new_meme):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme
            headers = {'Authorization': 'Bearer '}
            put_meme_endpoint.put_meme(id_meme, new_body, headers)
            put_meme_endpoint.check_status_code(401)

        # ==================== ПРАВА ДОСТУПА ====================

        @allure.story('Права доступа')
        @allure.title('Обновление мема, созданного другим пользователем')
        def test_put_meme_created_by_other_user(self, put_meme_endpoint, only_create_new_meme, api_headers_other_user):
            id_meme = only_create_new_meme
            new_body = meme_data.valid_body_for_post_meme
            put_meme_endpoint.put_meme(id_meme, new_body, api_headers_other_user)
            # Ожидаем 403 (Forbidden)
            put_meme_endpoint.check_status_code(403)

        # ==================== НЕКОРРЕКТНЫЕ МЕТОДЫ ====================

        @allure.story('Некорректные методы')
        @allure.title('Обновление мема через GET метод')
        def test_put_meme_with_get_method(self, get_one_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            get_one_meme_endpoint.get_meme_by_id(api_headers, id_meme)
            # Ожидаем 405 (Method Not Allowed)
            get_one_meme_endpoint.check_status_code(405)

        @allure.story('Некорректные методы')
        @allure.title('Обновление мема через POST метод')
        def test_put_meme_with_post_method(self, post_meme_endpoint, only_create_new_meme, api_headers):
            id_meme = only_create_new_meme
            post_meme_endpoint.post_meme({'some': 'data'}, api_headers)
            post_meme_endpoint.check_status_code(405)






