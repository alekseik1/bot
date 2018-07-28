import vk
import random

session = vk.Session()
api = vk.API(session, v=5.0)


def get_random_wall_picture(group_id):
    max_num = api.photos.get(owner_id=group_id, album_id='wall', count=0)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num)['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment

def get_random_wall_attachment(group_id):
    pass

def get_previous_interlocutors(token):
    dialogs = api.messages.getDialogs(access_token=token)
    ids = []
    for message in dialogs['items']:
        ids.append(message['user_id'])
    return ids

def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)


def get_wall_posts(token, group_id: str):
    """
    Получает все посты с указанной группы. Картинки и прочее медиа **игнорируются**.

    :param group_id: Номер группы vk
    :type group_id: str
    :return: Объект list, содержащий строковые сообщения.
    """

    # TODO: почему-то токен группы не подходит для данного запроса. Разберись с этим потом
    special_token = 'd85ec3aebcf1553c7b19ff2f8d561531d48a6785ae432e06154d435418ad6b25e9d04877ec5ef6d0e054a'
    session = vk.Session(access_token=token)
    api = vk.API(session, v=5.0)
    posts = api.wall.get(owner_id=group_id, count=1000, access_token=special_token)
    res = []
    for i in posts['items']:
        res.append(i['text'])
    return res
