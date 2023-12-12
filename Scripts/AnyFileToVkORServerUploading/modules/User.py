import unicodedata
import urllib.request
from PIL import Image
import random
import sqlite3
import json
import requests
import vk_api
import os


if str(os.name) == "nt":dir_pref = "\\"
else:dir_pref = "/"


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)

def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device
token = 'vk1.a.nM5nelhJ3Pz_5xxZiOHewLGZgwvhbQVdNGc92CAC8eYUwuMpdSZ9Q8j4Cn-8sXOQwufKAz0nDKh9i93xVWKyONNoYl4uBw4hDYJzFcaf9VwAee3x3fKwxEgGK0v8QO7qJj8PWCIoxWBHapzJeevvrNwPeEd2SBRNLtE-Z4bxM3JimERdry-XfKA_uEZMQ1WVgK5zcUsprux5MxUN4-0zcQ'
token_I = 'vk1.a.KEUma3WGK5BSfWeRk1Ie8JGsoX6gJU2_18zX344bQKvwpnWU1BoikZHSoL92Yk9yl9FeEwcupAXQ3q8O0fDiaIlVhWapz6uCnMSOZ6K53fHHV_0PQ40wd8029Q08aUFfBLOmH7Q82QuC7-LuhfqcWWNxzhc2wgsACxjah3QbhDrzkXyBboU141iYA2D42DxMf-dOseqlLgHHYg1e7bZMow'
tiken_ = 'https://oauth.vk.com/blank.html#access_token=vk1.a.KEUma3WGK5BSfWeRk1Ie8JGsoX6gJU2_18zX344bQKvwpnWU1BoikZHSoL92Yk9yl9FeEwcupAXQ3q8O0fDiaIlVhWapz6uCnMSOZ6K53fHHV_0PQ40wd8029Q08aUFfBLOmH7Q82QuC7-LuhfqcWWNxzhc2wgsACxjah3QbhDrzkXyBboU141iYA2D42DxMf-dOseqlLgHHYg1e7bZMow&expires_in=0&user_id=435600030&email=malayski51@gmail.com'


class User:
    """
        docstring forUser.

        Чтение конфигурации из файла
    """

    def __init__(self, file=rf'modules{dir_pref}config.json'):
        with open(file) as f:data = json.load(f)

        self.user_id = data['user_id']
        self.group_id = data['group_id']
        self.token = data['token']

        self.login = data['login']
        self.passwd= data['password']
        if data['auth_token'] == 1:
            self.vk = vk_api.VkApi(token = self.token)
        else:
            self.vk = vk_api.VkApi(
                                    self.login, self.passwd,
                                    captcha_handler=captcha_handler,
                                    auth_handler = auth_handler,
                                    app_id=6287487) #all - 6287487, my - 2685278
            self.vk.auth()
        self.v = data['v']



    """
        Загрузка изображения на сервер и получение объекта photo
    """

    def picture_send(self, image_to_send, working_directory):
        do = os.getcwd()
        os.chdir(working_directory)
        a = self.vk.method('photos.getWallUploadServer', {'v': self.v})
        b = requests.post(a['upload_url'], files={
                          'photo': open(image_to_send, 'rb')}).json()
        c = self.vk.method('photos.saveWallPhoto', {
            'photo': b['photo'], 'server': b['server'], 'hash': b['hash'], 'v': self.v})[0]
        d = f'photo{c["owner_id"]}_{c["id"]}'
        os.chdir(do)
        return d



    """
        Пост в группу
    """

    def make_post(self, attachments):
        self.post_text = ''
        
        
        self.vk.method('account.setOnline', {'v': self.v})
        id_ = self.vk.method('wall.post', {
                                           'owner_id': -self.group_id,
                                           'message': self.post_text,
                                            'attachments': attachments,
                                            'from_group': 1,
                                            'signed': 0,
                                            'v': self.v})
        
        return id_
    
    def delete_post(self, post_id):
        self.vk.method('account.setOnline', {'v': self.v})
        status = self.vk.method('wall.delete', {
                                           'owner_id': -self.group_id,
                                           'post_id' : post_id,
                                            'v': self.v
                                            })
        return status    



    def groups_getOnTheWallCustom(self, post_id):
        post_ = self.vk.method('wall.getById', {'posts': f'-{self.group_id}_{post_id}','v': self.v})[0]
        return post_
