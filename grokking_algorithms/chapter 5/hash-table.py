book = dict()
book['apple'] = 0.67
book['milk'] = 1.49
book['avocado'] = 1.49
print(book)
print(book['avocado'])

voted = {}


def check_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote!')


check_voter('tom')
check_voter('mike')
check_voter('mike')

cache = {}
get_data_from_server = None


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
