# Шахматный ферзь может ходить на любое число клеток по горизонтали,
# по вертикали или по диагонали. Даны две различные клетки шахматной доски,
# определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
# Для простоты можно не рассматривать случай, когда данные клетки совпадают.

# Формат входных данных
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

# Формат выходных данных
# Программа должна вывести YES, если из первой клетки ходом ферзя можно попасть во вторую.
# В противном случае - NO.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2:
    print('YES')
elif y1 == y2:
    print('YES')
elif abs(x2 - x1) == abs(y2 - y1):
    print('YES')
else:
    print('NO')
