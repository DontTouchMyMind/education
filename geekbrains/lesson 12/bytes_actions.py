# Common string
s = 'Hello world'

# String bytes
sb = b'Hello bytes'

# Index of common string
print(s[1])     # The result will be 'e'
# Index of string bytes
print(sb[1])    # The result will be '101'

# Slice of common string
print(s[1:3])   # The result will be 'el'
# Slice of string bytes
print(sb[1:3])  # The result will be "b'el'"

# Iterate over the string bytes in cycle
for item in sb:
    print(item)