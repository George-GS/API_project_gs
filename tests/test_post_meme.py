import allure

import meme_data

class TestPostMeme:

    def test_1(self, post_meme_endpoint, delete_meme_endpoint, api_headers):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, api_headers)
        post_meme_endpoint.check_status_code(200)

        delete_meme_endpoint.delete_meme(post_meme_endpoint.id_meme)



 @allure.story('Создание мема')
    @allure.title('Создание мема с валидными данными')
    def test_post_meme_success(self, post_meme_endpoint, api_headers):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, api_headers)
        post_meme_endpoint.check_status_code(200)
        post_meme_endpoint.check_response_has_id()

    @allure.story('Создание мема')
    @allure.title('Создание мема с пустым массивом тегов')
    def test_post_meme_empty_tags(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['tags'] = []
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)

    @allure.story('Создание мема')
    @allure.title('Создание мема с пустым массивом цветов')
    def test_post_meme_empty_colors(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['info']['colors'] = []
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)

    @allure.story('Создание мема')
    @allure.title('Создание мема с одним тегом')
    def test_post_meme_one_tag(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['tags'] = ['fun']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)

    @allure.story('Создание мема')
    @allure.title('Создание мема с одним цветом')
    def test_post_meme_one_color(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['info']['colors'] = ['green']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)

    @allure.story('Создание мема')
    @allure.title('Создание мема с разным порядком полей')
    def test_post_meme_different_order(self, post_meme_endpoint, api_headers):
        body = {
            "url": "https://s00.yaplakal.com/pics/pics_original/4/7/1/20258174.jpg",
            "tags": ["fun", "boy"],
            "text": "Seriously? Yes, seriously",
            "info": {
                "colors": ["green", "blue"]
            }
        }
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)

    # ==================== НЕГАТИВНЫЕ ТЕСТЫ (ОБЯЗАТЕЛЬНЫЕ ПОЛЯ) ====================

    @allure.story('Валидация')
    @allure.title('Создание мема с пустым телом запроса')
    def test_post_meme_empty_body(self, post_meme_endpoint, api_headers):
        post_meme_endpoint.post_meme({}, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема без поля text')
    def test_post_meme_missing_text(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['text']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема без поля url')
    def test_post_meme_missing_url(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['url']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема без поля tags')
    def test_post_meme_missing_tags(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['tags']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема без поля info')
    def test_post_meme_missing_info(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        del body['info']
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема без поля colors в info')
    def test_post_meme_missing_colors(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['info'] = {}
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    # ==================== НЕГАТИВНЫЕ ТЕСТЫ (НЕПРАВИЛЬНЫЕ ТИПЫ) ====================

    @allure.story('Валидация')
    @allure.title('Создание мема с пустым text')
    def test_post_meme_empty_text(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['text'] = ''
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема с пустым url')
    def test_post_meme_empty_url(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['url'] = ''
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема с неверным форматом url')
    def test_post_meme_invalid_url(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['url'] = 'not_a_valid_url'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема с tags не массивом')
    def test_post_meme_tags_not_array(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['tags'] = 'fun'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема с colors не массивом')
    def test_post_meme_colors_not_array(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['info']['colors'] = 'green'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Валидация')
    @allure.title('Создание мема с text не строкой')
    def test_post_meme_text_not_string(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['text'] = 12345
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    # ==================== ГРАНИЧНЫЕ ЗНАЧЕНИЯ ====================

    @allure.story('Граничные значения')
    @allure.title('Создание мема с очень длинным text')
    def test_post_meme_long_text(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['text'] = 'a' * 5000
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Граничные значения')
    @allure.title('Создание мема с очень длинным url')
    def test_post_meme_long_url(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['url'] = 'https://' + 'a' * 5000 + '.com'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    @allure.story('Граничные значения')
    @allure.title('Создание мема с множеством тегов')
    def test_post_meme_many_tags(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['tags'] = [f'tag_{i}' for i in range(100)]
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(400)

    # ==================== БЕЗОПАСНОСТЬ ====================

    @allure.story('Безопасность')
    @allure.title('Создание мема с XSS в тексте')
    def test_post_meme_xss_in_text(self, post_meme_endpoint, api_headers):
        body = meme_data.valid_body_for_post_meme.copy()
        body['text'] = '<script>alert(1)</script>'
        post_meme_endpoint.post_meme(body, api_headers)
        post_meme_endpoint.check_status_code(200)

    # ==================== АВТОРИЗАЦИЯ ====================

    @allure.story('Авторизация')
    @allure.title('Создание мема без токена')
    def test_post_meme_unauthorized(self, post_meme_endpoint):
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, {})
        post_meme_endpoint.check_status_code(401)

    @allure.story('Авторизация')
    @allure.title('Создание мема с невалидным токеном')
    def test_post_meme_invalid_token(self, post_meme_endpoint):
        headers = {'Authorization': 'Bearer invalid_token_12345'}
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, headers)
        post_meme_endpoint.check_status_code(401)

    @allure.story('Авторизация')
    @allure.title('Создание мема с пустым токеном')
    def test_post_meme_empty_token(self, post_meme_endpoint):
        headers = {'Authorization': 'Bearer '}
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, headers)
        post_meme_endpoint.check_status_code(401)