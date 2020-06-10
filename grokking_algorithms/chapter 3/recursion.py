def countdown(i):
    """
    A simple example of a recursion function.
    :param i: input counter
    :return: number of count
    """
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


# A simple example of a callstack fuctions.
def greet(name):
    print('hello, ' + name + '!')
    greet2(name)
    print('getting ready to say bye...')
    bye()


def greet2(name):
    print('how are you, ' + name + '?')


def bye():
    print('ok bye!')


def fact(x):
    """
    Function calculates factorial of a number.
    :param x: input number.
    :return: factorial of your number.
    """
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


if __name__ == '__main__':
    countdown(5)
    greet('Leo')
    print(fact(5))
