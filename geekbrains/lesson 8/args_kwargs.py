def greating(say, *name):   # * - after '*' we can pass as many arguments one by one
    print(say, name)        # The result will be a tuple of arguments


greating('hello', 'Leo')
greating('hello', 'Leo', 'Kate')
greating('hello', 'Leo', 'Kate', 'Max')

