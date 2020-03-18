# Open the file for writing bytes
with open('bytes.txt', 'wb') as f:
    f.write(b'Hello bytes')


# Reading as txt
with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

# Open the file for writing bytes
with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

# Reading as text with utf-8
with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())
