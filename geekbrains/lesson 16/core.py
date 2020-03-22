import os
import shutil
import datetime


def create_file(name, text=None):  # Function to create a file
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):  # Function to create a folder
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Error: "Folder alredy exists"')


def get_list(folders_only=False):  # Function display folders
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]  # if 'f' is dir
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        try:
            os.rmdir(name)
        except FileNotFoundError:
            print('Error:"It does not exist"')
    else:
        try:
            os.remove(name)
        except FileNotFoundError:
            print('Error:"It does not exist"')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Error:"This folder already exist"')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} -  {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':  # so that when importing into another scrips the code would not be executed
    create_file('text.dat', 'hello, im for test')
    create_folder('new_folder')
    get_list()
    get_list(True)
    # delete_file('text.dat1')
    # delete_file('new_folder')
    copy_file('new_folder', 'copy_folder')
    copy_file('text.dat', 'copy_text')
    save_info('abc')
