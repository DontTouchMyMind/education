import os

print(os.name)  # operating system name

print(os.getcwd())  # Current directory name

new_path = os.path.join(os.getcwd(), 'new_folder')  # Creating a new path

os.mkdir(new_path)  # Creating folder
