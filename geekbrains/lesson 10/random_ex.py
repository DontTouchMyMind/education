import random

# 1. Загадать случайное число от 0 до 100
print(random.randint(0, 100))
# 2. Выбрать победителя из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(random.choice(players))
# 3. Выбрать 3х победителей из списка
print(random.sample(players, 3))
# 4. Перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print(cards)
random.shuffle(cards)
print(cards)