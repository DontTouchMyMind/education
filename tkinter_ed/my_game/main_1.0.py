import random
from tkinter import *
from tkinter.messagebox import *

game_started = False
number = 0


def new_game():
    global number

    number = random.randint(0, 100)
    print(number)


if not game_started:
    new_game()

# Size game field
w_height = 300
w_width = 300

main_window = Tk()
main_window.title(f'{number} GUESS THE NUMBER')
main_window.resizable(width=False, height=False)

# Main screen position
real_h = main_window.winfo_screenheight()  # Your screen height
real_w = main_window.winfo_screenwidth()  # Your screen width
top_offset = (real_h - w_height) // 2  # Center of your screen in height
left_offset = (real_w - w_width) // 2  # Center of your screen in width
main_window.geometry(f'{w_width}x{w_height}+{left_offset}+{top_offset}')

bottom_frame = Frame(main_window)
bottom_frame.pack(side=BOTTOM)

entry1 = Entry(bottom_frame, width=3, font=15)
button1 = Button(bottom_frame, text='Check it', command=new_game)
label_result = Label(main_window, textvariable=number, width=27, font=15)
label_result.pack(fill=X, pady=20)

entry1.pack(side=LEFT)
button1.pack(side=LEFT)
# button1.bind('<Button-1>', new_game)

main_window.mainloop()
