import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('start')
command = sys.argv[1]
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
        print('Error: File name of Folder name is missing')
    else:
        copy_file(name, new_name)
elif command == 'help':
    print('Commands are...')
save_info('end')
