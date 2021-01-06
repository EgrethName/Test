import requests

url = 'https://stepic.org/favicon.ico'

response = requests.get(url)
data = response.text
print(response.headers)
print(data)
