numbers = [1, 5, 3, 5, 9, 7, 11]

print(sorted(numbers))  # ascending sorting

print(sorted(numbers, reverse=True))  # descending sorting

names = ['', 'Max', 'Kate', 'Rich', 'Any']

print(sorted(names))  # dictionary sorting

cities = [('Moscow', 1000), ('London', 1700), ('Paris', 2000)]
print(sorted(cities))


def by_count(city):
    return city[1]


print(sorted(cities, key=by_count))

print(sorted(cities, key=lambda x: x[1]))
