from tkinter import *

root = Tk()  # Create main window

top_frame = Frame(root)  # Create container
top_frame.pack()  # Display in the main window, Default side from pack is TOP

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text='Button 1', fg='red')
button2 = Button(top_frame, text='Button 2', fg='blue')
button3 = Button(top_frame, text='Button 3', fg='green')
button4 = Button(bottom_frame, text='Button 4', fg='grey')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

one = Label(root, text='ONE', bg='red', fg='yellow')
one.pack()
two = Label(root, text='TWO', bg='blue', fg='white')
two.pack(fill=X)
three = Label(root, text='THREE', bg='green', fg='grey')
three.pack(side=LEFT, fill=Y)

root.mainloop()
