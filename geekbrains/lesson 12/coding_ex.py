sb = b'Ad'

print(sb[0])    # ASCII code is 65
print(sb[1])    # ASCII code is 100

s = 'Hello world'
sb = s.encode('ascii')
print(sb)
print(type(sb))

s = 'Hello world мир'
sb = s.encode('utf-8')
print(sb)
print(type(sb))

# Decoding
s = sb.decode('utf-8')
print(s)
print(type(s))