from vk import *
import random, vk, time
token = "токен (VK ADMIN)"
user_id = "айди страницы" 
posts_id = "айди поста"
msgs = input("Введите сообщение: ")
session = vk.Session(access_token=token)
apivk = vk.API(session, v = 5.95)
while True:
    try:
        print(apivk.wall.createComment(owner_id=user_id, post_id=posts_id, message=msgs, guid=random.randint(0, 9999999999)))
    except:
        pass
    time.sleep(3)
