import requests


key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDUxNTA3MDIsImlhdCI6MTc0NDk4MjcwMiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjY5ZmFjNTlmMjY1MTVjYjE3OTI0OGQxYjQ0NzkyNjE5ODM1NjYwZmUwMDA5YWFiNzI4ZjQ0YTNiMjgzYWIyMDUiLCJ0eXBlIjoxMH0.VOSokSy_UG_CcDAe1m3vtc1q2T_IQ-KDVR3ae-bMqNU"
my_headers = {
    'Authorization': f'Bearer {key}'
    }

class ChitaiGorodAPI:
    def __init__(self, url):
        self.url = url

    def serch_product(self,phrase):
        params = {
            'phrase': phrase
            }
        response = requests.get(self.url, params=params, headers=my_headers)
        return response
