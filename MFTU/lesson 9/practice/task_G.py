# Напечатайте входную строку, отсортировав ее по возрастанию ASCII
# кода символов.
#
# Входные данные
#   Строка, заканчивающаяся точкой,
#   длиной не более 1000 символов. Точку сортировать не нужно.
#   Все, что находится после первой точки - игнорировать.
#
# Выходные данные
#   Отсортированная строка с точкой на конце.
def hoar_sort(input_list):
    """
    Function sorts input-list.
    :param input_list: input-list
    :return: sorted list
    """
    if len(input_list) <= 1:
        return
    barrier = input_list[0]
    left_list = []  # < barrier
    middle_list = []  # = barrier
    right_list = []  # > barrier
    for x in input_list:
        if x < barrier:
            left_list.append(x)
        elif x == barrier:
            middle_list.append(x)
        else:
            right_list.append(x)
    hoar_sort(left_list)
    hoar_sort(right_list)
    k = 0
    for x in left_list + middle_list + right_list:
        input_list[k] = x
        k += 1


def check_hoar_sort(sort_algorithm):
    print('TEST', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    input_data = [1, 3, 4, 22, 5]
    sorted_data = [1, 3, 4, 5, 22]
    sort_algorithm(input_data)
    print('Ok' if input_data == sorted_data else 'Fail')

    print('TEST', sort_algorithm.__doc__)
    print('testcase #2: ', end='')
    input_data = list(range(10, 20)) + list(range(0, 10))
    sorted_data = list(range(0, 20))
    sort_algorithm(input_data)
    print('Ok' if input_data == sorted_data else 'Fail')


if __name__ == '__main__':
    check_hoar_sort(hoar_sort)
    data = input()
    input_list = []
    count = 0
    while count < len(data):
        if data[count] == '.':
            break
        input_list.append(ord(data[count]))
        count += 1
    hoar_sort(input_list)
    for k in range(len(input_list)):
        print(chr(input_list[k]), end='')
    print('.')
