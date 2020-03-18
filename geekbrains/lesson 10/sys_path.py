import sys

print(sys.path)
print(type(sys.path))

for p in sys.path:
    print(p)

sys.path.append('D:')

