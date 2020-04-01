def hello():  # Function definition
    print('Hello world')


def hello_name(name):
    print('Hello,', name)


def max2(x, y):
    if x > y:
        return x
    else:
        return y


def max3(x, y, z):
    return max2(x, max2(y, z))


def hello_separated(name='World', separator='-'):
    print('Hello', name, sep=separator)


hello()  # Function call

f = hello  # Synonym for function

f()  # Function call

hello_name('Max')

var1 = int(input('Enter X: '))
var2 = int(input('Enter Y: '))
var3 = int(input('Enter Z: '))

print(max2(var1, var2))
print(max2('кит', 'кот'))
print(max2('кот', 'котенок'))
print(max3(var1, var2, var3))
print(max3(3.4, 7, 1.1))
print(max3('b', 'abc', 'abd'))
hello_separated()
hello_separated('Max', '***')
hello_separated(separator='***')
hello_separated(separator='***', name='John')
