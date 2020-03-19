# 1. Create a list from random numbers from 1 to 100
import random

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# 2. Create a list of square of numbers
numbers = [number**2 for number in numbers]
print(numbers)
# 3. Create a list of names starting with letter A
names = ['Anna', 'Max', 'Leo', 'Alice']

names = [name for name in names if name.startswith('A')]
print(names)