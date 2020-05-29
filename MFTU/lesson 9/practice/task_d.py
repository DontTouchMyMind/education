# Студент покупает рис каждый день.
# В первую неделю рис стоит price монет.
# Каждый день (перед началом рабочего дня) цена риса
# увеличивается на delta монет (price = price + delta).
# Неделя - 7 дней.
# Студент покупал рис m недель.
#
# Написать программу (с циклом while),
# которая вычисляет сколько денег потратил студент.


data = [int(n) for n in input().split()]
price = data[0]
delta = data[1]
m = data[2]
day = m * 7
money = data[0]
while day > 1:
    price = price + delta
    day -= 1
    money = money + price
print(money)
