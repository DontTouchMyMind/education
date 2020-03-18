import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 345]},
    {'name': 'Leo', 'age': 33}
]
print(type(friends))

# Conversion list of friends to json
json_friends = json.dumps(friends)

print(json_friends)
print(type(json_friends))

# Reconversion from json to list
friends = json.loads(json_friends)
print(friends)
print(type(friends))