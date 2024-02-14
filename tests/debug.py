import json
import os.path

import requests
import soundfile as sf
# print(sf.available_formats())

# authorization_url = ('https://www.googleapis.com/identitytoolkit/v3/'
#                      'relyingparty/verifyPassword?key=AIzaSyCxu7mVxd_waBDUn9VKblBl4zl8MX5WxWY')
# data_default_user = {"email": "autoTestSpecialist@brainup.spb.ru", "password": "password", "returnSecureToken": "true"}


# def record():
#     task_id = int(input('Input task id:'))
#     """
#     params: task_id = int
#     returns all audio from selected card in .ogg format.
#     """
#     result_post = requests.post(authorization_url, data_default_user)
#     id_token = json.loads(result_post.text)['idToken']  # Highlight the token value
#     # print(id_token)
#     result_get = requests.get(f'https://brainup.site/api/tasks/{str(task_id)}',
#                               headers={'Content-Type': 'application/json',
#                                        'Authorization': 'Bearer {}'.format(id_token)})
#     word = json.loads(result_get.text)['data']["answerOptions"][0]['word']
#     amount_words = len(json.loads(result_get.text)['data']["answerOptions"])
#     words = [json.loads(result_get.text)['data']["answerOptions"][i]['word'] for i in range(amount_words)]
#     print(words)
#     for word in words:
#         result2 = requests.get(f'https://brainup.site/api/audio?text={word}&locale=en-us&exerciseId=919',
#                                headers={'Content-Type': 'application/json',
#                                         'Authorization': 'Bearer {}'.format(id_token)})
#         try:
#             os.mkdir('../audio')
#             print('Directory audio created!')
#         except Exception as ex:
#             pass
#         file_path = os.path.join('../audio/')
#         # print(result_get.content)
#         with open(file_path + f'{word}.ogg', "wb") as file:
#             binary_data = result2.content
#             # Example binary data
#             file.write(binary_data)
#
#         # Указание пути к исходному файлу .ogg
#         input_file = file_path + f'{word}.ogg'
#
#         # Указание пути для сохранения файла .wav
#         output_file = file_path + f'{word}.wav'
#
#         # Загрузка аудио из исходного файла .ogg
#         audio, samplerate = sf.read(input_file)
#         print(sf.info(input_file))
#
#         # Сохранение аудио в файл .wav
#         sf.write(output_file, audio, samplerate)
#
# record()
#
# path_env = os.path.join('../audio/')  # Path(r'C:\Users\User\PycharmProjects\auto-tests-python\audio')
# data = []
# x = os.getcwd()
# for w in os.walk(path_env):
#     for s in w[2]:
#         data.append(x + '\\audio\\' + s)
# print(data)

# result = ['Время: 0 мин, 15 сек', 'Всего заданий: 9', 'Повторений: 0', 'Неправильных ответов: 1']
