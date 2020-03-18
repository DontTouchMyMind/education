# Read the object from the file

# Open file
with open('person.dat', 'rb') as f:
    # we should to know, how was the object write
    # read file as list
    result = f.readlines()

# Recreate the original object
person ={}
# First element is name
person['name']= result[0].decode('utf-8').replace('\n', '')
# The next is phones
phones = []
for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))
person['phones'] = phones
print(person)
