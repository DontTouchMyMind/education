import random
from tkinter import *
from tkinter.messagebox import *

game_started = False
number = 0


def new_game():
    global number
    number = random.randint(0, 100)
    print(number)


def user_data():  # check user input
    global user_number, is_winner

    user_number = entry1.get()

    try:
        if int(user_number) == number:
            label_result['text'] = 'Вы победили!'
            is_winner = True
            win_condition()
        elif int(user_number) > number:
            label_result['text'] = 'Ваше число больше загаданного!'
        else:
            label_result['text'] = 'Ваше число меньше загаданного!'
    except ValueError:
        label_result['text'] = 'Введите число от 0 до 100'


def win_condition():
    if is_winner == True:
        answer = askokcancel('AskRetryCancel', 'do you want to play more?')
        if answer == True:
            new_game()
        else:
            exit_app()


def exit_app():  # exit
    main_window.destroy()


if not game_started:
    new_game()

# Size game field
w_height = 300
w_width = 300

main_window = Tk()
main_menu = Menu(main_window)  # Drop-down menu
main_window.title('GUESS THE NUMBER')
main_window.resizable(width=False, height=False)

# Main screen position
real_h = main_window.winfo_screenheight()  # Your screen height
real_w = main_window.winfo_screenwidth()  # Your screen width
top_offset = (real_h - w_height) // 2  # Center of your screen in height
left_offset = (real_w - w_width) // 2  # Center of your screen in width
main_window.geometry(f'{w_width}x{w_height}+{left_offset}+{top_offset}')

drop_menu_item_1 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Game', menu=drop_menu_item_1)
drop_menu_item_1.add_command(label='New Game', command=new_game)  # should to add command and bitmap
drop_menu_item_1.add_command(label='Setting')  # should to add command
drop_menu_item_1.add_separator()
drop_menu_item_1.add_command(label='Exit', command=exit_app)  # should to add command

drop_menu_item_2 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Info', menu=drop_menu_item_2)
drop_menu_item_2.add_command(label='Stats')  # should to add command
drop_menu_item_2.add_separator()
drop_menu_item_2.add_command(label='Help')  # should to add command

bottom_frame = Frame(main_window)
bottom_frame.pack(side=BOTTOM)

entry1 = Entry(bottom_frame, width=3, font=15)
button1 = Button(bottom_frame, text='Check it', command=user_data)
label_result = Label(main_window, width=27, font=15)
label_result.pack(fill=X, pady=20)

entry1.pack(side=LEFT)
button1.pack(side=LEFT)
# button1.bind('<Button-1>', user_data)

main_window.mainloop()
