# Числа Фибоначи
n = 5
fib = [0, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
print(fib)


# Сколько различных траекторий "допрыгать" n,
# если прыгать можно +1 и +2 клетки.


def traj_num(n):
    k = [0, 1] + [0] * n
    for i in range(2, n + 1):
        k[i] = k[i - 2] + k[i - 1]
    return k[n]


# Усложним задачу, сделав запрешенные клетки и добавив действие
# Запрещенные клетки будем передавать списком и
# проверять принадлежит ли клетка этому списку.
def count_trajectories(n, allowed: list):
    k = [0, 1, int(allowed[2])] + [0] * (n - 3)
    for i in range(3, n + 1):
        if allowed[i]:
            k[i] = k[i - 1] + k[i - 2] + k[i - 3]
    return k(n)


# Минимальная стоимость достижения клетки n
# price[i] - цена посещения конкретной клетки
# C[i] - минимальная суммарная стоимость достижения клетки i
def count_min_cost(n, price: list):
    C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    return C[n]
