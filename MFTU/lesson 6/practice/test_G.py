# Пусть задана строка s. Назовем ее k-ой (k > 0) степенью s^k строку s^k = sss (k раз).
#   Например, третьей степенью строки abc является строка аbсаbсаbс.
#
# Корнем k степени из строки s называется такая строка t (если она существует), что t^k = s.
#
# Ваша задача состоит в том, чтобы написать программу, находящую степень строки или корень из нее.
#
# Формат входных данных
#   На вход программе подается 2 строки. Первая содержит строку S, вторая - степень k.
#   Отрицательная степень означает взятие корня соответствующей степени.
#
# Формат выходных данных
#   Вывести строку, являющуюуся ответом на задачу.
#   Если такой строки нет, то нужно вывести 'NO SOLUTION' (без кавычек).


input_data = input()
k = int(input())


def crate_sub_string():
    in_range = len(input_data) / input_data.count(input_data[0])
    result = input_data[0:int(in_range)]
    return result


t = crate_sub_string()

if k >= 0:
    print(input_data * k)
else:
    if t * abs(k) == input_data:
        print(t)
    else:
        print('NO SOLUTION')
