def hello():  # Function definition
    print('Hello world')


def hello_name(name):
    print('Hello,', name)


def max2(x, y):
    if x > y:
        return x
    else:
        return y


hello()  # Function call

f = hello  # Synonym for function

f()  # Function call

hello_name('Max')

var1 = int(input('Enter X: '))
var2 = int(input('Enter Y: '))
print(max2(var1, var2))
