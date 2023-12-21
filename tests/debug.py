import json

import requests

"""Авторизация дефолтного пользователя"""
result = requests.post(
    'https://www.googleapis.com/identitytoolkit/v3'
    '/relyingparty/verifyPassword?key=AIzaSyCxu7mVxd_waBDUn9VKblBl4zl8MX5WxWY',
    {"email": "default@default.ru", "password": "password", "returnSecureToken": "true"})
# print("Получаем ответ:\n", result.text)

id_token = json.loads(result.text)['idToken']  # выделяем значение токена

result = requests.get('https://brainup.site/api/tasks/919',
                      headers={'Content-Type': 'application/json',
                               'Authorization': 'Bearer {}'.format(id_token)})
# print(result.text)

result2 = requests.get('https://brainup.site/api/audio?text=mother&locale=en-us&exerciseId=919',
                       headers={'Content-Type': 'application/json',
                                'Authorization': 'Bearer {}'.format(id_token)})
print(result2.content)
with open('1.ogg', "wb") as file:
    binary_data = result2.content
    # Example binary data
    file.write(binary_data)
