# Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.


#from .practical_task_1 import create_folder
import practical_task_1
#import practical_task_2
from practical_task_2 import max_list, test_2, my_list
import sys

command = sys.argv[1]

if command == '1':
    practical_task_1.create_folder()
elif command == '2':
    practical_task_1.delete_folder()
elif command == '3':
    max_list()

