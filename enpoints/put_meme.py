import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class PutMeme(BaseEndpoint):
    '''

    '''

    @allure.step('')
    def put_meme(self, id_meme, body):
        ''''''
        self.response = requests.put(f'{self.BASE_URL}/meme/{id_meme}', json=body)
        return self.response
