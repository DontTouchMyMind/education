# Matrix transpose
matrix = [
    [0.5, 0, 0, 0, 0],
    [1, 0.5, 0, 0, 0],
    [1, 1, 0.5, 0, 0],
    [1, 1, 1, 0.5, 0],
    [1, 1, 1, 1, 0.5]
]
# Output on display
print(matrix)
print('-' * 17)
for row in matrix:
    print(row)
print('-' * 17)
# Classic method using zip function
matrix_t = zip(matrix[0], matrix[1], matrix[2], matrix[3], matrix[4])
for el in matrix_t:  # Result is tuple
    print(el)
print('-' * 17)

# Simple method
matrix_t = zip(*matrix)
for el in matrix_t:  # Result is list
    print(list(el))
