def greating(say, *args):   # * - after '*' we can pass as many arguments one by one
    print(say, args)        # The result will be a tuple of arguments


greating('hello', 'Leo')
greating('hello', 'Leo', 'Kate')
greating('hello', 'Leo', 'Kate', 'Max')

