def hello_max():
    print('Hello, Max')


def hello(name):
    print('Hello, ', name)


hello_max()
hello('Leo')
hello('Max')


def greating(name, say):
    print(say, name)


greating('Max', 'Hi')
greating('Kate', 'Good day')

# Function call with explicit parameters
greating(say='hello', name='Loe')   # U can pass parameters in any order


