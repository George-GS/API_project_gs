import allure

import meme_data

@allure.title('Получение всех мемов')
def test_get_objects_positive(get_all_memes_endpoint, api_headers):
    get_all_memes_endpoint.get_all_memes(api_headers)
    get_all_memes_endpoint.check_status_code(200)
    get_all_memes_endpoint.check_body_all_memes()

@allure.title('Получение всех мемов без авторизаци')
def test_get_all_memes_unauthorized(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(meme_data.headers_no_token)
    get_all_memes_endpoint.check_status_code(401)


@allure.title('Получение всех мемов c невалидным токеном')
def test_get_all_memes_with_bad_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(meme_data.headers_bad_token)
    get_all_memes_endpoint.check_status_code(401)


@allure.title('Получение всех мемов c пустым токеном')
def test_get_all_memes_with_empty_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(meme_data.headers_empty_token)
    get_all_memes_endpoint.check_status_code(500)

@allure.title('Получение списка мемов через POST метод')
def test_get_all_memes_wrong_method(get_all_memes_endpoint, api_headers):
    get_all_memes_endpoint.get_all_memes_post_method(api_headers)
    get_all_memes_endpoint.check_status_code(500)
