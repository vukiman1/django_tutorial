import requests
from todo_app.settings import settings


def get_data_from_api(api_url, api_key):
    response = requests.get(api_url, headers={"X-Api-Key": api_key})
    return response.json()
