# String
s = 'abc'

# Classic method
if len(s) != 0:
    print('The string is not empty')
else:
    print('The string is empty')

# Python method
if s:
    print('The string is not empty')
else:
    print('The string is empty')

# list and dictionary
l = [1, 2, 3]
d = {1: 'a'}

# Classic method
if  len(l) != 0 and len(d) != 0:
    print('list and dict are not empty')
else:
    print('list and dict are empty')

if l and d:
    print('list and dict are not empty')
else:
    print('list and dict are empty')

