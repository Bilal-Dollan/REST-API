import requests

endpoint = 'http://127.0.0.1:8000/api/products/'
data = {
    'title': 'good morining'
}
get_response = requests.get(endpoint, json=data)
print(get_response.json())
