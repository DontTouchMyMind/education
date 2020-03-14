cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris']

print(type(cities))
print(cities)

cities = set(cities)
print(type(cities))
print(cities)

cities = {'Las Vegas', 'Paris', 'Moscow'}
cities.add('London')
print(cities)
cities.add('Burma')
print(cities)

cities.remove('Moscow')
print(cities)

print(len(cities))

print('Paris' in cities)

for city in cities:
    print(city)