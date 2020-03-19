import math

numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# Create list from numbers that have square root of less than 2
result = []

# Classic method
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        if sqrt < 2:
            result.append(number)
print(result)

result = []

# with AND
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)

# with generator
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)