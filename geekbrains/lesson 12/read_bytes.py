# Open the file for writing bytes
with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир')


# Reading text as bytes
with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    # decode to get the string
    s = result.decode('utf-8')
    print(s)