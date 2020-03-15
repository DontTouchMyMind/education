cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)

cities.add('Berlin')
cities.add('London')
print(cities)

cities.remove('Moscow')
print(cities)

print(len(cities))
print('London' in cities)

for city in cities:
    print(city)