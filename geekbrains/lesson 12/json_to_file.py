import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 345]},
    {'name': 'Leo', 'age': 33}
]
print(type(friends))

# Open file
with open('friends.jon', 'w') as f:
    # Convert the list of friends to json and save the file
    json_friends = json.dump(friends, f)

# Reconversion from json to list
with open('friends.jon', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))
