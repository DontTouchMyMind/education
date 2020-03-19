import math
# Operator "AND"
if 1 > 2 and math.sqrt(-1):
    print('The will be no error, because "1 > 2" is False')
print('next step')

# if you swap condition
# if math.sqrt(-1) and 1 > 2:
#     print('The will be no error, because "1 > 2" is False')

# First False
print([1] and [] and '' and 1)      # The result will be first false. Its []

# Last True
print([1] and 1 and 20 and 1.1)     # The result will be last True. Its 1.1

# Operator "OR"
if 2 > 1 or math.sqrt(-1):
    print('The will be no error, because "2 > 1" is True')

# First True
print(0 or [] or 8 or 5)        # The result will be first true. Its 8

# Last false
print(0 or [] or () or {})      # The result will be last false. Its {}