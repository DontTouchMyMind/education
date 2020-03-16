def greating(say, *args):  # * - after '*' we can pass as many arguments one by one
    print(say, args)  # The result will be a tuple of arguments


greating('hello', 'Leo')
greating('hello', 'Leo', 'Kate')
greating('hello', 'Leo', 'Kate', 'Max')


def get_person(**kwargs):
    for k, v in kwargs.items():  # The result will be a dictionary of arguments
        print(k, v)


get_person(name='Leo', age=20, has_car=True)
