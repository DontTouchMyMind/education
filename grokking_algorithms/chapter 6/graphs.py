from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['tom'] = []
graph['jonny'] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('you')

search_queue = deque()
search_queue += graph['you']

while search_queue:  # Пока очередь не пуста
    person = search_queue.popleft()  # из очереди извлекается первый человек
    if person_is_seller(person):  # проверяем, является ли этот человек продавцом
        print(person + ' is a mango seller!')  # Да, это продавец манго
        break
    else:
        search_queue += graph[person]  # Нет, не является. Все друзья добавляются в очередеь поиска
else:
    print('false')  # Если выполнение дошло до этой строки, то продавцов нет
