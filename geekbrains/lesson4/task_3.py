# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет: [5, 8]

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
new_list = []
for num in my_list_1:
    while num in my_list_1:
        my_list_1.remove(num)
new_list = my_list_1
print(new_list)

# Будем отслеживать кол-во входов
numbers = [2, 2, 5, 12, 8, 2, 12]
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print(result)