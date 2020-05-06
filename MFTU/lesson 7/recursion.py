def matryoshka(n):
    if n == 1:
        print('Матрешечка')
    else:
        print('Вверх матрешки n=', n)
        matryoshka(n - 1)
        print('Низ матрешки n=', n)


matryoshka(5)
