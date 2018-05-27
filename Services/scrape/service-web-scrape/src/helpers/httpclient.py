import requests


class HttpClient():
    
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

    def get(self, url, headers=None):
        headers = headers is None and self.headers or headers
        request = requests.get(url, headers=headers)
        return request.text
