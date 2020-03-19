# слово -> СлОвО
word = 'рефрежератор'

result = []

for i in range(len(word)):
    letter = word[i].lower() if i % 2 != 0 else word[i].upper()
    result.append(letter)

result = ''.join(result)  # conversion from list to string
print(result)