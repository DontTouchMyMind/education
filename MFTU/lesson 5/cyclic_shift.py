def cyclic_shift_left(input_list, len_list):
    """
    Function take a list, their length and return the shifted left list.
    :param input_list: input list, type: list
    :param len_list: length of input list, type:int
    :return: shifted input list
    """
    tmp = input_list[0]
    for i in range(len_list - 1):
        input_list[i] = input_list[i + 1]
    input_list[len_list - 1] = tmp


def cyclic_shift_right(input_list, len_list):
    """
    Function take a list, their length and return the shifted right list.
    :param input_list: input list, type: list
    :param len_list: length of input list, type:int
    :return: shifted input list
    """
    tmp = input_list[len_list - 1]
    for i in range(len_list - 2, -1, -1):
        input_list[i + 1] = input_list[i]
    input_list[0] = tmp


def test_left():
    test_list_1 = [1, 2, 3, 4, 5]
    cyclic_shift_left(test_list_1, 5)
    if test_list_1 == [2, 3, 4, 5, 1]:
        print('#test_left - ok')
    else:
        print('#test_left - fail')


def test_right():
    test_list_1 = [1, 2, 3, 4, 5]
    cyclic_shift_right(test_list_1, 5)
    if test_list_1 == [5, 1, 2, 3, 4]:
        print('#test_right - ok')
    else:
        print('#test_right - fail')


if __name__ == '__main__':
    test_left()
    test_right()
