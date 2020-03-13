friend_name = 'Max'                 # Type is string
friends = ['Leo', 'Kate', 'Rick']   # Type is list
roles = ('admin', 'user', 'quest')  # Type is tuple

if  'Leo' in friends:
    print('i have this friend')

if 'M' in friend_name:
    print('Letter M is in name of my friend')

# For
for friend in friends:
    print(friend)

print('end for')

for letter in friend_name:
    print(letter)

for role in roles:
    print(role)
# While
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1
print('end while')