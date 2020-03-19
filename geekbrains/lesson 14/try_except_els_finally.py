number = int(input('Enter your number'))
try:
    result = 100 / number
except ZeroDivisionError as e:
    print('Error: Attempt to divide by 0 ', e)
else:
    print('All right')
finally:
    print('will aways be done')