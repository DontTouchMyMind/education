from tkinter import *


def output(event):
    txt = entry1.get()
    try:
        if int(txt) < 18:
            label1['text'] = 'U are very small'
        else:
            label1['text'] = 'Welcome!'
    except ValueError:
        label1['text'] = 'Its not correctly'


root = Tk()
root.title('How old are U?')
entry1 = Entry(root, width=3, font=15)
button1 = Button(root, text='Check it')
label1 = Label(root, width=27, font=15)

entry1.grid(row=0, column=0)
button1.grid(row=0, column=1)
label1.grid(row=0, column=2)

button1.bind('<Button-1>', output)  # "Button-1" is left mouse click

root.mainloop()
