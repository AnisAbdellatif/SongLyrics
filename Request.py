import requests

class Request:
    def __init__(self):
        pass

    @staticmethod
    def GET(URL, params={}, headers={}):
        res = requests.get(
            URL,
            params = params,
            headers = headers
        )
        return res.json()["response"]