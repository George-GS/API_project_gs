import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetObjects(BaseEndpoint):

    def get_objects(self, headers):
        self.response = requests.get(f'{self.BASE_URL}/meme', headers=headers)
        return self.response
