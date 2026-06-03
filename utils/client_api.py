import requests

class Api:
    BASE_URL = "https://gorest.co.in/public/v2/"

    def __init__(self):
        self.header = {
            "Authorization": "Bearer 960d5d19171b99e10290804ccac7f519081bb06596ccee50061375c33c00d331",
            "Content-type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url=url, headers=self.header)
        return response