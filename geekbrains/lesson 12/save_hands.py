person = {'name': 'Max', 'phones': [123, 345]}

# Open file
with open('person.dat', 'wb') as f:
    # For example, write an object to the file line by line
    # Firstly, take the name
    name = person['name']
    # add line break, encoding to bytes and write this
    f.write(f'{name}\n'.encode('utf-8'))
    # Take the phone
    phones = person['phones']
    # writing each phone to new string
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('the object was write')