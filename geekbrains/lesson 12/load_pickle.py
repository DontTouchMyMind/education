import pickle

# Open the file
with open('person.dat', 'rb') as f:
    person = pickle.load(f)

print(person)
