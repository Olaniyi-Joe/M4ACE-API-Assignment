import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={'query': 'Hello World'})
response = get_response.json()
print(response.get('url', 'not available'))

data = response.get('data')

# print(data)
