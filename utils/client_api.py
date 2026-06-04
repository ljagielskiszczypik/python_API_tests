import requests

class Api:
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    def __init__(self):
        self.header = {
            "Content-type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url=url, headers=self.header)
        return response

    def post(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url=url, headers=self.header, json=data)
        return response

    def put(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url=url, headers=self.header, json=data)
        return response

    def patch(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.patch(url=url, headers=self.header, json=data)
        return response