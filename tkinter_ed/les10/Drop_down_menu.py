from tkinter import *


def new_win():
    win = Toplevel(root)
    label1 = Label(win, text='Text on TopWindow level', font=20)
    label1.pack()


def exit_app():
    root.destroy()  # Уничтожаем главное окно и всех его потомков


root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label='File', menu=first_item)
first_item.add_command(label='New', command=new_win)
first_item.add_command(label='Exit', command=exit_app)

second_item = Menu(main_menu, tearoff=0)  # tearoff=0 запретит отрывать меню от гл. окна
main_menu.add_cascade(label='Edit', menu=second_item)
second_item.add_command(label='Item1')
second_item.add_command(label='Item2')
second_item.add_command(label='Item3')
second_item.add_separator()
second_item.add_command(label='Item4')

root.mainloop()
