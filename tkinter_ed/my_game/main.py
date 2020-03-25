from tkinter import *  # import tkinter as tk
import random

number = random.randint(1, 100)
user_number = 0
is_winner = False  # Win condition


def new_win():  # Create new game
    pass


def exit_app():  # exit
    main_window.destroy()


def output(event):  # check user input
    global user_number

    user_number = entry1.get()  # should to add exception!
    if int(user_number) == number:
        label_result['text'] = 'Вы победили!'
    elif int(user_number) > number:
        label_result['text'] = 'Ваше число больше загаданного!'
    else:
        label_result['text'] = 'Ваше число меньше загаданного!'


# Size window
G_HEIGHT = 300
G_WIDTH = 600

# Create game fields
main_window = Tk()
main_menu = Menu(main_window)  # Drop-down menu
main_window.title('GUESS THE NUMBER')
main_window.configure(menu=main_menu, bg='red')  # how can i change color to .png or .bmp???
main_window.resizable(width=False, height=False)  # Cannot resize window
# main_window.iconbitmap('???.ico')

# Main screen position
real_h = main_window.winfo_screenheight()  # Your screen height
real_w = main_window.winfo_screenwidth()  # Your screen width
top_offset = (real_h - G_HEIGHT) // 2  # Center of your screen in height
left_offset = (real_w - G_WIDTH) // 2  # Center of your screen in width
main_window.geometry(f'{G_WIDTH}x{G_HEIGHT}+{left_offset}+{top_offset}')

# Drop_down menu

drop_menu_item_1 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Game', menu=drop_menu_item_1)
drop_menu_item_1.add_command(label='New Game')  # should to add command and bitmap
drop_menu_item_1.add_command(label='Setting')  # should to add command
drop_menu_item_1.add_separator()
drop_menu_item_1.add_command(label='Exit', command=exit_app)  # should to add command

drop_menu_item_2 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Info', menu=drop_menu_item_2)
drop_menu_item_2.add_command(label='Stats')  # should to add command
drop_menu_item_2.add_separator()
drop_menu_item_2.add_command(label='Help')  # should to add command

# Game tools

bottom_frame = Frame(main_window)
bottom_frame.pack(side=BOTTOM)

label_welcome = Label(main_window, text='Welcome to Guess the Number', font=15)
label_welcome.pack(fill=X, pady=20)
label_rules = Label(main_window, text='Enter your NUMBER', font=15)
label_rules.pack(fill=X, pady=20)
label_result = Label(main_window, width=27, font=15)
label_result.pack(fill=X, pady=20)

entry1 = Entry(bottom_frame, width=3, font=15)
button1 = Button(bottom_frame, text='Check it')
label_was_entered = Label(bottom_frame, width=27, font=15)

entry1.pack(side=LEFT)
button1.pack(side=LEFT)
label_was_entered.pack(side=LEFT)

button1.bind('<Button-1>', output)

main_window.mainloop()
