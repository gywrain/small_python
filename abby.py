import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'YWJjMTMzMGItMmI2MC00OGQ1LTg0OGUtYWFjMGNlZDU3NTA4OjA2ZWVjZTRjYjU5NDQ4MGI4MGMzNTA2YTQwMzY4M2M5'
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
	token = auth.text
	
	while True:
		word = input('Введите слово для перевода: ')
		if word:
			headers_translate = {
				'Authorization': 'Bearer ' + token
			}
			params = {
				'text': word,
				'srcLang': 1033,
				'dstLang': 1049
			}
			r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
			res = r.json()
			try:
				print(res['Translation']['Translation'])
			except:
				print('Не найдено варианта для перевода')			
else:
	print('Error')
