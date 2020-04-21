# The sum of the digits of a three-digit number

number = int(input('Enter your number: '))
result = 0
while number > 0:
    digit = number % 10
    number //= 10
    result += digit

print(f'The sum of digit is {result}')
