import pickle

person = {'name': 'Max', 'phones': [123, 345]}

# Open the file
with open('person.dat', 'wb') as f:
    pickle.dump(person, f)

print('Object was write')
