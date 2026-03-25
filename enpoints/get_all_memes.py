import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class GetAllMemes(BaseEndpoint):
    '''

    '''
    @allure.step('')
    def get_all_memes(self, headers):
        self.response = requests.get(f'{self.BASE_URL}/meme', headers=headers)
        return self.response
