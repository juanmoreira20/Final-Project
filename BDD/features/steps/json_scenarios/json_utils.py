import requests
import json


def get_url():
    return 'webpage'

def get_valid_credentials():
    return {'login': 'login credentials', 'password': 'password credentials'}

def get_token():
    url = get_url()
    credentials_body = get_valid_credentials()

    response = requests.post(f'{url}/authenticate/login', json=credentials_body)

    json_data = json.loads(response.text)

    token = json_data['token']

    auth = f'Bearer {token}'

    return auth
