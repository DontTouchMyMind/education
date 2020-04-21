# The sum of the digits of a three-digit number
number = int(input('Enter your number: '))
result = 0
while number > 0:
    digit = int(number % 10)
    number //= 10
    result += digit
print(int(result))
