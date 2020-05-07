# Вы - водитель грузовика с открытым кузовом. В кузове два груза: пианино и холодильник.
# Пианино необходимо доставить в институт, холодильник в общежитие.
# В каждое из этих мест ведет отдельная дорога, начинающаяся от перекрестка,
# на котором Вы стоите, других дорог в мире нет.
# Известно, что по дороге в институт есть мост,
# на котором действует ограничение максимальной допустимой массы автомобиля с грузом,
# а по дороге в общежитие есть туннель с ограничением высоты.
# Требуется определить, возможно ли доставить грузы или нет
# (разумеется, сгружать их, где попало, Вам запрещено).
#
# Формат входных данных
#   На вход подается 8 чисел натуральных чисел (каждое < 100),
#   каждое в новой строке, в следующем порядке:            [i]
#       вес грузовика без груза,                            0
#       высота платформы кузова (на которой стоят грузы),   1
#       вес пианино,                                        2
#       высота пианино,                                     3
#       вес холодильника,                                   4
#       высота холодильника,                                5
#       максимальный допустимый вес на мосту,               6
#       максимальная допустимая высота в туннеле            7
#
# Примечание: пианино и холодильник заведомо возвышаются над кабиной грузовика,
# т.е. высоту кабины можно в расчет не принимать.
#
# Формат выходных данных
#   Вывести YES если доставка возможна и NO в противном случае.


def check_weight(weight_car, weight_piano, weight_frost, max_weight):
    """
    Function calculates the maximum weight of the car with a load
    and calculates whether the car will pass over the bridge.
    """
    sum_weight = weight_car + weight_piano + weight_frost
    return True if sum_weight <= max_weight else False


def check_height(height_car, height_piano, height_frost, max_height):
    """
    Function calculates the maximum weight of the car with a load
    and calculates whether the car will pass through the tunnel.
    """
    sum_height = max(height_frost, height_piano) + height_car
    return True if sum_height <= max_height else False


def test_function(function_under_test):
    print('Testing: ', function_under_test.__doc__)
    print('testcase #1: ', end='')
    input_data = [1, 10, 10, 11]
    result = function_under_test(*input_data)
    print('Ok' if result else 'Fail')

    print('Testing: ', function_under_test.__doc__)
    print('testcase #2: ', end='')
    input_data = [1, 5, 1, 3]
    result = function_under_test(*input_data)
    print('Ok' if not result else 'Fail')

    print('Testing: ', function_under_test.__doc__)
    print('testcase #3: ', end='')
    input_data = [10, 5, 151, 800]
    result = function_under_test(*input_data)
    print('Ok' if result else 'Fail')


numbers = []

for i in range(8):
    x = int(input())
    if x > 100:
        break
    numbers.append(x)

result_weight = check_weight(numbers[0], numbers[2], numbers[4], numbers[6])
result_height = check_height(numbers[1], numbers[3], numbers[5], numbers[7])
print('YES' if result_weight and result_height else 'NO')

# if __name__ == '__main__':
#     test_function(check_weight)
#     test_function(check_height)
