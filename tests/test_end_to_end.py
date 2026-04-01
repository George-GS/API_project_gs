import allure
import pytest

import meme_data


class TestMemeLifecycle:
    '''Класс для end to end теста'''

    @allure.title('E2E тест(полный жизненный цикл мема)')
    def test_meme_lifecycle(
        self,
        post_authorize_endpoint,
        get_authorize_token_endpoint,
        post_meme_endpoint,
        put_meme_endpoint,
        get_one_meme_endpoint,
        get_all_memes_endpoint,
        delete_meme_endpoint,
        dynamic_api_headers,
    ):

        # Получаем токен из заголовков
        token = dynamic_api_headers['Authorization']

        # 1. Проверка токена
        get_authorize_token_endpoint.check_token(token)
        get_authorize_token_endpoint.check_status_code(200)
        get_authorize_token_endpoint.check_text_get_token()

        # 2. Создание мема
        post_meme_endpoint.post_meme(meme_data.valid_body_for_post_meme, dynamic_api_headers)
        post_meme_endpoint.check_status_code(200)
        post_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)
        meme_id = post_meme_endpoint.id_meme

        # 3. Получение мема по id после создания
        get_one_meme_endpoint.get_meme_by_id(meme_id, dynamic_api_headers)
        get_one_meme_endpoint.check_status_code(200)
        get_one_meme_endpoint.check_body_response(meme_data.valid_body_for_post_meme)

        # 4. Обновление мема (PUT)
        upd_body = meme_data.valid_body_for_put_meme.copy()
        upd_body['id'] = meme_id
        put_meme_endpoint.put_meme(meme_id, upd_body, dynamic_api_headers)
        put_meme_endpoint.check_status_code(200)
        put_meme_endpoint.check_body_response(upd_body)

        # 5. Получение мема по id после обновления
        get_one_meme_endpoint.get_meme_by_id(meme_id, dynamic_api_headers)
        get_one_meme_endpoint.check_status_code(200)
        get_one_meme_endpoint.check_body_response(upd_body)

        # 6. Удаление мема
        delete_meme_endpoint.delete_meme(meme_id, dynamic_api_headers)
        delete_meme_endpoint.check_status_code(200)
        delete_meme_endpoint.check_response_text(f'Meme with id {meme_id} successfully deleted')

        # 7. Проверка, что мем удалён
        get_one_meme_endpoint.get_meme_by_id(meme_id, dynamic_api_headers)
        get_one_meme_endpoint.check_status_code(404)
