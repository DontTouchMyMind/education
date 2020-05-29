# Сколько раз цифра d входит в десятичную запись числа n?
#
# Входные данные
#   Число 0≤d≤9. Пробел. Целое положительное число n
#   в десятичной системе (0 ≤ n ≤ 3·10 6) .
#
# Выходные данные
#   Сколько раз цифра d входит в запись числа n.


data = [n for n in input().split()]
print((data[1]).count(data[0]))

# with WHILE
count = 0
data = [int(n) for n in input().split()]
while data[1] > 0:
    if data[1] % 10 == data[0]:
        count += 1
    data[1] = data[1] // 10
print(count)
