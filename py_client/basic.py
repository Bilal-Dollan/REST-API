import requests


endpoint = 'http://127.0.0.1:8000/'

get_response = requests.get(endpoint, json = {'hello': 'HIIII'})
print(get_response.status_code)