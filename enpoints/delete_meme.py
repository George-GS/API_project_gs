import requests
import allure

from enpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):
    '''

    '''

    @allure.step('')
    def delete_meme(self, id_meme):
        self.response = requests.delete(f'{self.BASE_URL}/meme/{id_meme}')
        return self.response