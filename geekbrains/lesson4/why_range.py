# Когда нам может помочь range

winners = ['Max', 'Leo', 'Kate']

# простой перебор
for winner in winners:
    print(winner)
# что делать если нам нужно вывести менсто победителя?
# использовать while
# или есть способ лучше?
for i in range(len(winners)):
    #print(i)
    print(i+1, ')', winners[i])
# Вывести нечетные цифры от 1 до 5
numbers = [1, 3, 5]

for number in numbers:
    print(number)

print(list(range(1, 20, 2)))

for number in range(1, 20, 2):
    print(number)
#
#
#
#
#
#