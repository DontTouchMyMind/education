friend = {
    'name': 'Max',
    'age': '23',
    'has_car': True
}

# по ключам
for key in friend.keys():
    print(key)
    print(friend[key])
# по значениям
for val in friend.values():
    print(val)

# по паре ключ - значение
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)