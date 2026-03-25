import allure

import meme_data

@allure.title('Получение списка всех мемов')
def test_get_objects_positive(get_all_memes_endpoint, api_headers):
    get_all_memes_endpoint.get_all_memes(api_headers)
    get_all_memes_endpoint.check_status_code(200)







