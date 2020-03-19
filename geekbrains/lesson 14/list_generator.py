# Write only positive numbers to the list

numbers = [1, 2, 3, 4, 5, -1, -2, -3]

# Classic method
result = []
for number in numbers:
    if number > 0:
        result.append(number)

print(result)

# Using 'filter' function
result = filter(lambda number: number > 0, numbers)
print(list(result))

# Using list-generator
result = [number for number in numbers if number > 0]
print(result)