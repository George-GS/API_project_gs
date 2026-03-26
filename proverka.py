import requests

BASE_URL = 'http://memesapi.course.qa-practice.com'

headers = {'Authorization': 'x0KXQUmXyZ9DuE4'}
headers_1 = {}
# response = requests.get(f'{BASE_URL}/meme/1', headers=headers)
response1 = requests.get(f'{BASE_URL}/meme/1', headers=headers_1)
print(response1.text)