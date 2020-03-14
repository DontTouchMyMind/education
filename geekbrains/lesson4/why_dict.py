friend = {
    'name': 'Max',
    'age': '23'
}

print(friend['age'])

friend['has_car'] = True    # Добавили ключ+переменную
print(friend)

friend['has_car'] = False
print(friend)

del friend['age']
print(friend)

if 'age' in friend:
    print('Есть возраст')

if 'has_car' in friend:
    print('Есть машина')