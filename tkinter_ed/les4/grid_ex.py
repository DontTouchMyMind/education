from tkinter import *

root = Tk()

label_1 = Label(root, text='NAME')
label_2 = Label(root, text='PASSWORD')

entry_1 = Entry(root)  # Widget for entering the text(data?)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text='Stay in the system')
c.grid(columnspan=2)

root.mainloop()
