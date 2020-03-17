import modA
from folderB.modB import foo, bar
# import modC #не выполнится ничего
from modC import foo    # Выполнится foo
print(modA.foo)
modA.bar()

print(foo)
bar()