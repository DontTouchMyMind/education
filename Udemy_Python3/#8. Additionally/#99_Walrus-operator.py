import random

walrus = False
print(walrus)

print(walrus := True)  # В Python 3.8.
print(type(walrus))

# Без walrus.
rows = input('Enter the number of rows: ')
for i in range(int(rows)):
    print('*' * (i + 1))
print(f'Number of rows:{rows}')

# Используя walrus.
for i in range(rows := int(input('Enter the number of rows: '))):
    print('*' * (i + 1))
print(f'Number of rows:{rows}')


# Без walrus.
def read_file(fp):
    while True:
        line = fp.readline()
        if not line:
            break
        split_line = line.splite()
        print(split_line[1])


# Используя walrus.
def read_file2(fp):
    while line := fp.readline():
        if not line:
            break
        split_line = line.splite()
        print(split_line[1])


# Без walrus.
def get_mode():
    return 's' if random.randint(1, 10) > 5 else None


mode = get_mode()
if mode:
    full_mode_name = 'silent' if mode == 's' else 'unknown'
    print(f'processing in {full_mode_name} mode')

# Используя walrus.
if mode := get_mode():
    full_mode_name = 'silent' if mode == 's' else 'unknown'
    print(f'processing in {full_mode_name} mode')
