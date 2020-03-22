def unlucky_number(number):
    if number == 13:
        raise ValueError('Error: "Unlucky number"')  # calling exception
    else:
        return number ** 2


number = int(input('Enter the number'))
try:
    result = unlucky_number(number)
except ValueError:  # Exception handling
    print('U have unlucky number')
else:
    print(result)
