import requests

BASE_URL = 'http://memesapi.course.qa-practice.com'

headers = {'Authorization': 'x0KXQUmXyZ9DuE4'}

response = requests.get(f'{BASE_URL}/meme/1', headers=headers)
print(response.json())