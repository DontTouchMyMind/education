from tkinter import *


class Question:

    def __init__(self, main):  # __init__ - constructor

        self.entry1 = Entry(main, width=3, font=15)  # Class attributes always begin with 'self'
        self.button1 = Button(main, text='Check it')
        self.label1 = Label(main, width=27, font=15)

        self.entry1.grid(row=0, column=0)
        self.button1.grid(row=0, column=1)
        self.label1.grid(row=0, column=2)

        self.button1.bind('<Button-1>', self.answer)

    def answer(self, event):

        txt = self.entry1.get()

        try:
            if int(txt) < 18:
                self.label1['text'] = 'U are very small'
            else:
                self.label1['text'] = 'Welcome!'
        except ValueError:
            self.label1['text'] = 'Its not correctly'


root = Tk()
root.title('How old are U?')
q = Question(root)

root.mainloop()
