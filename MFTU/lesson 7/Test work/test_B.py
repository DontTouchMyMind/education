# Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.
#
# Формат входных данных
#   Даны три натуральных числа – стороны треугольника.
#   Каждое число вводится с новой строки.
#
# Формат выходных данных
#   Необходимо вывести одно из слов:
#       right для прямоугольного треугольника,
#       acute для остроугольного треугольника,
#       obtuse для тупоугольного треугольника
#       или impossible, треугольника с такими сторонами не существует.


def sort(input_list):
    """
    Bubble sort function
    :param input_list:
    :return: sorted list
    """
    for bypass in range(1, len(input_list)):
        for i in range(0, len(input_list) - bypass):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]


leg_a = int(input())
leg_b = int(input())
leg_c = int(input())
my_list = [leg_a, leg_b, leg_c]
if (leg_a + leg_b) > leg_c and (leg_a + leg_c) > leg_b and (leg_b + leg_c) > leg_a:

    sort(my_list)
    h = my_list[2]
    k = my_list[1]
    l = my_list[0]

    if h ** 2 == k ** 2 + l ** 2:
        print('right')
    elif h ** 2 < k ** 2 + l ** 2:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')
