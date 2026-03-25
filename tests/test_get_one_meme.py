import allure

import meme_data

def test_get_one(get_one_meme_endpoint, api_headers):
    get_one_meme_endpoint.get_meme_by_id(api_headers, 1)
    get_one_meme_endpoint.check_status_code_200()
    get_one_meme_endpoint.check_body_response(meme_data.body_meme_id_1)
