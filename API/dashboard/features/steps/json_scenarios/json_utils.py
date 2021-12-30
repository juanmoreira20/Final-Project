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

def get_id():
    url = get_url()
    token = get_token()
    header = {'authorization': token}

    response = requests.get(f'{url}/companies', headers=header)
    assert response.status_code == 200

    json_data = json.loads(response.text)

    id = json_data[0]['id']

    return id
