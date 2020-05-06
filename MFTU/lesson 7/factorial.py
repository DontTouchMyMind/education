def factorial_function(n: int):
    assert n >= 0, 'Factorial not defined'
    if n == 0:
        return 1
    return factorial_function(n - 1) * n


n = int(input())
print(factorial_function(n))
