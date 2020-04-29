# a = ['###', '@', '??'] a.sort(key=lambda x: len(x)) a ['@', '??', '###']
# a.sort(key=lambda x: len(x), reverse=True) ['###', '??', '@']

number = int(input())
my_dict = {}
result = []
while True:
    input_data = input()
    if input_data == '#':
        break
    student_id, value = map(int, input_data.split())
    if student_id in my_dict:
        my_dict[student_id][0] += value
        my_dict[student_id][1].append(value)
    else:
        my_dict[student_id] = [value, [value]]

result = sum((sorted(value, reverse=True)
              for student_id, value in sorted(my_dict.values(), reverse=True)), [])

print(result)
print(*result)
r1 = sorted(my_dict.values(), reverse=True)
print(r1)
r2 = sum((sorted(value, reverse=False) for student_id, value in r1), [])
print(r2)
