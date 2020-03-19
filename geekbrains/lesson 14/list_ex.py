a = 1
b = a
b = 100

print(a)    # the result will be 1

a = [1, 2, 3]
b = a
b[1] = 100
print(a)    # the result will be [1, 100, 3]

numbers = [1, 2, 3]


def change_number_in_list(input_list):
    input_list[1] = 200

# after call function
change_number_in_list(numbers)

# the list also change in the main program!!!
print(numbers)

# Slice copy
print('# Slice copy')
a = [1, 2, 3]
b = a[:]
b[1] = 100
print(a)

# Method .copy
print('# Method .copy')
b = a.copy()
b[1] = 222
print(a)
print('*****************************')
# Methods slice and .copy will not wor if we have nested lists
a = [1, 2, [1, 2]]
b = a[:]
b[2][1] = 200
print(a)

b = a.copy()
b[2][1] = 300
print(a)        # these methods copy first part of list and exclude second part

# Method deep copy
import copy

a = [1, 2, [1, 2]]

b = copy.deepcopy(a)
b[2][1] = 200
print(a)    # Deep copy
