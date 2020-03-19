# слово -> СлОвО
word = 'слово'

result = []

for i in range(len(word)):
    if i % 2 != 0:
        letter = word[i].lower()
    else:
        letter = word[i].upper()
    result.append(letter)

result = ''.join(result)  # conversion from list to string
print(result)