import requests
from config import MY_TOKEN, MY_USER_AGENT


my_headers = {
    'authorization': f'Bearer {MY_TOKEN}',
    'User-Agent': MY_USER_AGENT
    }

class ChitaiGorodAPI:
    def __init__(self, url):
        self.url = url

    def search_product(self,phrase):
        params = {
            'phrase': phrase
            }
        response = requests.get(self.url, params=params, headers=my_headers)
        return response
