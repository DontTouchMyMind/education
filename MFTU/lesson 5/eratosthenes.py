n = int(input('Enter the number to which you want to find primes: '))
numbers = [True] * n
numbers[0] = numbers[1] = False
for i in range(2, n):
    if numbers[i]:
        for j in range(2 * i, n, i):
            numbers[j] = False
for i in range(n):
    print(i, '-', 'prime' if numbers[i] else 'composite')
