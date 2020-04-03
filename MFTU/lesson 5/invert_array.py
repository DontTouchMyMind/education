def invert_array(input_list: list, N: int):
    """
    Обращение массива (поворот задом-наперед)
    в рамках индексов от 0 до N-1
    :param input_list:
    :param N:
    :return:
    """
    for k in range(N // 2):
        input_list[k], input_list[N - 1 - k] = input_list[N - 1 - k], input_list[k]


def test_invert_array():
    list_1 = [1, 2, 3, 4, 5]
    print(list_1)
    invert_array(list_1, 5)
    print(list_1)
    if list_1 == [5, 4, 3, 2, 1]:
        print('#test1 - ok')
    else:
        print('#test1 - fail')

    list_2 = [0, 0, 0, 0, 0, 10]
    print(list_2)
    invert_array(list_2, 6)
    print(list_2)
    if list_2 == [10, 0, 0, 0, 0, 0]:
        print('#test2 - ok')
    else:
        print('#test2 - fail')


test_invert_array()
