def array_search(A: list, N: int, x: int):
    """
    Осуществляет поиск числа х в массиве А,
    в диапазоне от 0 до N-1 индекса включительно.
    Если в массиве несколько одинаковых элементов,
    равных х, то вернуть индекс первого по счету.
    :param A:
    :param N:
    :param x:
    :return: индекс элемента x в массиве А.
            Или -1, если такого нет.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print('#test 1 - ok')
    else:
        print('#test 1 - fail')

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print('#test 2 - ok')
    else:
        print('#test 2 - fail')

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print('#test 3 - ok')
    else:
        print('#test 3 - fail')


test_array_search()
