# 1. В консольный файловый менеджер добавить проверку ввода пользователя
# для всех функции с параметрами (на уроке разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером.
# Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.
import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game_reverse import game_reverse
from game import game

save_info('start')
try:
    command = sys.argv[1]
except IndexError:
    print('Error: Command is missing. Use .help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Error: File name is missing')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Error: Folder name is missing')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Error: File name of Folder name is missing')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Error: File name or Folder name is missing')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('Commands are...')
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Error: Path for directory is missing')
        else:
            change_dir(name)
    elif command == 'game':
        game()
    elif command == 'game_reverse':
        game_reverse()
    save_info('end')
