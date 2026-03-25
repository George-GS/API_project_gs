import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetOneObject(BaseEndpoint):
    """

    """

    @allure.step('')
    def get_object_by_id(self, headers, id_obj):
        self.response = requests.get(f'{self.BASE_URL}/meme/{id_obj}', headers=headers)
        return self.response

    @allure.step('')
    def check_body_response(self, body_response):
        assert self.response.json() == body_response
