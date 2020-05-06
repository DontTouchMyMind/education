my_list = []

x = int(input())
my_list.append(x)  # Добавить в конец

print(len(my_list))

x = my_list.pop()  # Удалить с конца

# List comprehension

A = [x ** 2 for x in range(10)]

# common method

B = []
for x in range(10):
    B.append(x ** 2)
# Common method
C = [1, 2, 3, 4, -5, -2]
C_new = []
for x in C:
    if x % 2 == 0:
        C_new.append(x ** 2)

# List comprehension
C_new_2 = [x ** 2 for x in C if x % 2 == 0]
# ternal operator
C_new_3 = [(0 if x < 0 else x ** 2) for x in C if x % 2 == 0]
print(C_new_3)
