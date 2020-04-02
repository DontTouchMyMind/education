a = [1, 2, 3, 4, 5]

for x in a:
    print(x, type(x))
    x += 1
    print(x)
print(a)

# Square each element of the array

for k in range(5):
    a[k] = a[k] ** a[k]
print(a)

# My method

a = [1, 2, 3, 4, 5]
a = [x ** 2 for x in a]
print(a)

a = [0] * 5
top = 0
x = int(input())
while x != 0:
    a[top] = x
    top += 1
    x = int(input())
for k in range(4, -1, -1):
    print(a[k])
