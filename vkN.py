from vk import *
import random, vk, time
token = "5fce3b8b59bca9dbe45d4e587efd7b42082c7e33b7f41986b241601f6ea574e880f6779b50c62ac98edc9"
user_id = "648505320" 
posts_id = "648505320_31"
msgs = input("хто я ")
session = vk.Session(access_token=token)
apivk = vk.API(session, v = 5.95)
while True:
    try:
        print(apivk.wall.createComment(owner_id=user_id, post_id=posts_id, message=msgs, guid=random.randint(0, 9999999999)))
    except:
        pass
    time.sleep(3)
