# Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание.
# Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.
pl_name = input('choose your name: ')
en_name = input('choose enemy name: ')

player = {
    'name': pl_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2,
    }

enemy = {
    'name': en_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2,
}


def attack(person1, person2):

    def func_1(damage, armor):
        total = damage / armor
        return total

    total_damage = int(func_1(person2['damage'], person1['armor']))
    person1['health'] = person1['health'] - total_damage

attack(player, enemy)

# Validating of function
print(player)

