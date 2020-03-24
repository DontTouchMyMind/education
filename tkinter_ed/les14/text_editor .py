from tkinter import *
from tkinter.filedialog import *


def open_file():
    of = askopenfilename()
    file = open(of, 'r')
    txt.insert(END, file.read())  # Хотим вставить в конец виджета txt, то что у нас попадет в file
    file.close()


def save_file():
    sf = asksaveasfilename()  # Этой инструкцией мы вызываем диалоговое окно, кот позволит сохранить файл
    final_text = txt.get(1.0, END)  # Должны получить содержимое всего виджета txt
    file = open(sf, 'w')  # Открываем файл на перезапись, если его нет, то будет создан
    file.write(final_text)
    file.close()


def exit_app():
    root.quit()


root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=first_item)

first_item.add_command(label='Open', command=open_file)

first_item.add_command(label='Save', command=save_file)

first_item.add_command(label='Exit', command=exit_app)

txt = Text(root, width=40, height=15, font=12)
txt.pack(expand=YES, fill=BOTH)  # С этими двумя параметрами виджет текст будет растягиваться по всей ширине и высоте

root.mainloop()
