# Задача "про шахматного короля".
def king(n: int, m: int):
    """
    Функция считает сколько доступных траекторий существует,
    что бы добраться до заданной точки, если можем двигаться
    только вправо и вниз на 1 клетку.
    :param n: type:int; Первая координата заданной точки.
    :param m: type:int; Вторая координата заданной точки.
    :return: type:int; Кол-во возможных траекторий.
    """
    K = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            K[i][j] = K[i][j - 1] + K[i - 1][j]
            if K[i][j] == 0:
                K[i][j] = 1
    return K[n][m]


# Наибольшая общая подпоследавательность.


def len_gcs(A, B):  # greatest common subsequence
    """
    Функция расчитывает длину наибольшей общей подпоследовательности.
    :param A: Первая последовательность.
    :param B: Вторая последовательность.
    :return: type: int; Длинна наибольшей общей подпоследовательности.
    """
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]  # F[len(A)][len(B)]


if __name__ == '__main__':
    print(king(6, 6))
    print(len_gcs([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]))
    print(len_gcs('fork', 'work'))
