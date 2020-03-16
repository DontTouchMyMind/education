def my_func(my_var):
    my_var = 999
    print('Inside function:', my_var)


print("Example 1")
a = 1
my_func(a)
print('After function call:', a)


def some_func():
    a = 888
    print('Inside function:', a)


print('Example 2')
a = 1
some_func()
print('After function call:', a)

global_var = 1


def func():
    global global_var  # If u want to change global variable
    local_var = 100
    print(local_var)
    print(global_var)
    global_var = 55  # U cant do that without str.26 (without 'global _name_var_')


print('Example 3')
func()
print(global_var)  # The result will be "55"
