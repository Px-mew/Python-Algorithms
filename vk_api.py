"""Нахождение наиболее короткой цепочки друзей между двумя пользователями ВК"""
import requests
import time
# progress bar
from tqdm import tqdm 
from collections import deque

def get_friends_list(id_user):
    """Запрос и получение списка друзей"""
    r = requests.get(HOST + 'friends.get', params = {'user_id': id_user, 'access_token': access_token, 'v': VERSION})
    if 'response' in r.json():
        return r.json()['response']['items']
    return []

HOST = 'https://api.vk.com/method/'
# Версия  API
VERSION = '5.74'
# Получить токен
access_token = ""

r = requests.get(HOST + 'users.get', params = {'user_ids': '552775031, 199302012', 'access_token': access_token, 'v': VERSION})

id_start = 552775031
id_end = 199302012

# Создание очереди
queue = deque(get_friends_list(id_start))
# Словарь расстояний и предков для каждой ячейки
distances = {v: 1 for v in queue}
parents = {v: 552775031 for v in queue}

while id_end not in distances:
    cur_user = queue.popleft()
    new_users = get_friends_list(cur_user)
    time.sleep(0.2)
    for u in tqdm(new_users):
        if u not in distances:
            queue.append(u)
            distances[u] = distances[cur_user]+1
            parents[u] = cur_user

path = [id_end]
parent = parents[id_end]
parents[id_start] = None
while not parent is None:
    path.append(parent)
    parent = parents[parent]

print(path)