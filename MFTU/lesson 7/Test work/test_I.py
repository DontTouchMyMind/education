# В некотором физическом эксперименте показания прибора снимались с частотой 5 измерений в секунду.
# Эксперимент проводился в течение довольно большого времени, и в результате накопилось очень много данных.
# Ученых, которые проводили данный эксперимент, очень интересует,
# какое максимальное значение измеряемой величины достигалось во время измерения.
# Но вот беда: на остановку установки также требуется секунда времени,
# и в течение этого времени с установки могут приходить совершенно любые значения величины.
# В связи с этим, показания последних 5 измерений учитывать при поиске максимального значения не следует.
#
# Вам необходимо написать программу, которая в данном потоке
# чисел заранее неизвестной длины находит максимальное значение, отбрасывая при этом последние 5 измерений.
#
# Формат входных данных
#   На вход вашей программе передается последовательность натуральных чисел -- результаты измерений.
#   Каждое новое число передается с новой строки.
#   Гарантируется, что длина входной последовательности не меньше 6 и не превосходит 10 9 .
#   На конце последовательности передается число 0.
#
# Формат выходных данных
#   Программа должна вывести на экран одно число --
#   максимальное значение входной последовательности за исключением последних 5 элементов.

numbers = []
result = 0
x = 0
while True:
    number = int(input())
    if number == 0:
        break
    numbers.append(number)
    if len(numbers) > 5:
        x = numbers.pop(0)
    result = result if result > x else x

print(result)