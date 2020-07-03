def fib_rec(n):
    """
    Рекурентный способ вычисления числа фибоначи.
    :param n: type:int; номер по порядку в ряде Фибоначи.
    :return: type:int; число Фибоначи.
    """
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib(n):
    """
    Вычисление числа фибоначи методом динамического программирования.
    :param n: type:int; номер по порядку в ряде Фибоначи.
    :return: type:int; номер по порядку в ряде Фибоначи.
    """
    F = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


def traj_num(n):
    """
    Колличество траекторий достичь точки n из точки 1, можно двигаться +1, +2, +3 клетки.
    :param n: type:int; целевая клетка.
    :return: type:int; кол-во возможных траекторий.
    """
    k = [0, 1] + [0] * n
    for i in range(3, n + 1):
        k[i] = k[i - 3] + k[i - 2] + k[i - 1]
    return k[n]


def count_min_cost(n, price: list):
    """
    Минимальная стоимость достижения клетки n.
    :param n: type:int; целевая клетка.
    :param price: type:list; список стоимостей посещения каждой клетки.
    :return: минимальная суммарная стоимость достижения заданной клетки.
    """
    C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    return C[n]


def count_min_cost_path(n, price: list):
    """
    Функция вычисляет по какому пути прошел кузнечик.
    :param n: type:int; целевая клетка.
    :param price: type:list; список стоимостей посещения каждой клетки.
    :return: type:list; список вершин через которые прошел кузнечик.
    """
    C = [0] * (n + 1)
    C[1] = price[1]
    for i in range(2, n + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    path = []
    i = n
    while i > 0:
        if C[i - 1] < C[i - 2]:
            prev = i - 1
        else:
            prev = i - 2
        path.append(prev)
        i = prev
    path.append(0)
    path = path[::-1]
    return path


def king(n: int, m: int):
    """
    Функция вычисляет сколькими способами шахматный король
    может добраться до заданной клетке на доске,
    если он может двигаться 3-мя способами:
    вправо, вниз, вниз-вправо(по горизонтали).
    :param n: type:int; первая координата целевой клетки.
    :param m: type:int; вторая координата целевой клетки.
    :return: type:int; количство возможных траекторий.
    """
    desk = [[0] * (m + 1) for i in range(n + 1)]
    desk[0][0] = 1
    print(desk)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            desk[i][j] = desk[i - 1][j] + desk[i][j - 1] + desk[i - 1][j - 1]
    print(desk)
    return desk[n][m]


if __name__ == '__main__':
    print(fib_rec(5))
    print(fib(5))
    print(traj_num(5))
    print(count_min_cost(5, [0, 1, 2, 3, 4, 5]))
    print(count_min_cost_path(5, [0, 1, 2, 3, 4, 5]))
    print(king(4, 5))
