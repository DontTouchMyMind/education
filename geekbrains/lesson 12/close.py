f = open('first.txt', 'r')

for line in f:
    print(line.replace('\n', ''))

f.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')