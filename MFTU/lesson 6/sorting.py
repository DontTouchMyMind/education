def insert_sort(input_list):
    """
    Функция сортирует список вставками.
    Function sorts the list by inserts.
    :param input_list:
    :return:
    """
    n = len(input_list)
    for top in range(1, n):
        k = top
        while k > 0 and input_list[k - 1] > input_list[k]:
            input_list[k], input_list[k - 1] = input_list[k - 1], input_list[k]
            k -= 1


def choiсe_sort(input_list):
    """
    Функция сортирует список выбором.
    Function sorts the list by choice
    :param input_list:
    :return:
    """
    n = len(input_list)
    for position in range(0, n - 1):
        for k in range(position + 1, n):
            if input_list[k] < input_list[position]:
                input_list[k], input_list[position] = input_list[position], input_list[k]


def bubble_sort(input_list):
    """
    Функция сортирует лист методом пузырька
    Function sorts the list by bubble's method
    :param input_list:
    :return:
    """
    n = len(input_list)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if input_list[k] > input_list[k + 1]:
                input_list[k], input_list[k + 1] = input_list[k + 1], input_list[k]


# Опережающее тестирование гарантирует безошибочную работу алгоритма!!!
# Testing drive development


def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    input_list = [4, 2, 5, 1, 3]
    sorted_list = [1, 2, 3, 4, 5]
    sort_algorithm(input_list)
    # if input_list == sorted_list:   # Выполеняется долго требует len(input_list) операций
    #     print('Ok')
    # else:
    #     print('Fail')
    print('Ok' if input_list == sorted_list else 'Fail')

    print('testcase #2: ', end='')
    input_list = list(range(10, 20)) + list(range(0, 10))
    sorted_list = list(range(20))
    sort_algorithm(input_list)
    print('Ok' if input_list == sorted_list else 'Fail')

    print('testcase #3: ', end='')
    input_list = [4, 2, 4, 2, 1]
    sorted_list = [1, 2, 2, 4, 4]
    sort_algorithm(input_list)
    print('Ok' if input_list == sorted_list else 'Fail')


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choiсe_sort)
    test_sort(bubble_sort)
