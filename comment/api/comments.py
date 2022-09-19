import requests
from urllib.parse import urljoin

BASE_URL = 'http://127.0.0.1:8000/'


class ApiComment:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',

    }

    @staticmethod
    def response_handler(response):
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'接口异常: {response.status_code}')

    def get_api(self, url, params=None):
        url = urljoin(BASE_URL, url)
        response = requests.get(url=url, headers=self.headers, params=params)
        return self.response_handler(response)

    def post_api(self, url, data=None, json=None):
        url = urljoin(BASE_URL, url)
        response = requests.post(url=url, headers=self.headers, data=data, json=json)
        return self.response_handler(response)

    def add_token(self,url,data):
        login_response = self.post_api(url,data=data)
        self.headers['Authorization'] = login_response['data']['token']
        return login_response


api = ApiComment()
if __name__ == '__main__':
    login_data = {'username':'test','password':'123456'}
    login_url = '/api/login/'
    api.add_token(login_url,login_data)
    print(api.get_api('/api/subjects/'))
