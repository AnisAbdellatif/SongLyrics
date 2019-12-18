import urllib.parse
import os
import json

import requests
from Request import Request
from bs4 import BeautifulSoup

class GeniusAPI:    
    @staticmethod
    def search(query):
        query = urllib.parse.quote(query)
        dir = os.path.dirname(__file__)
        with open(f'{dir}/config.json') as json_data_file:
            config = json.load(json_data_file)

        # You should go into config.json and put your Ganius API Key
        API = config["API_KEYS"]["GENIUS_API"]
        url = f"https://api.genius.com/search?q={query}"
        headers = {'Authorization': f'Bearer {API}'}
        data = Request.GET(url , headers=headers)
        return data["hits"]
    
    @staticmethod
    def fetchLyrics(path):
        url = f"https://genius.com{path}"
        print(url)
        page = requests.get(url)
        if page.status_code == 404:
            return None

        html = BeautifulSoup(page.text, "html.parser")
        div = html.find("div", class_="lyrics")
        if not div:
            return None

        lyrics = div.get_text()
        return lyrics
