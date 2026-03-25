import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class PostMeme(BaseEndpoint):
    '''

    '''
    @allure.step('')
    def post_meme(self, body):
        self.response = requests.post(f'{self.BASE_URL}/meme', json=body)
        self.id_meme = self.response.json()['id']
        return self.response






