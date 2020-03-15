
base = int(input('Enter your calculation system: '))
x = int(input('Enter your number: '))

while x > 0:            # "пока есть цифры"
    digit = x % base    # Взять последнюю цифру "бери последнюю цифру"
    print(digit, end='')# "Печатай ее"
    x //= base          # Зачекнуть последнюю цифру "И отрывай ее"
