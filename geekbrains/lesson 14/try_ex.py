number = int(input('Enter your number'))
try:
    result = 100 / number
except ZeroDivisionError:
    print('Error: Attempt to divide by 0 ')
except Exception:
    print('Error: Unknown Error')
