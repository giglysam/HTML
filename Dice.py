from tkinter import *
import random
root = Tk()
root.resizable(False, False)
r = [1, 2, 3, 4, 5, 6]
r0 = random.choice(r)
a = Label(root, text=str(r0))
a.pack()

a0 = Entry(root, width=2)
a0.pack()


def b(event):
    global r0
    r0 = random.choice(r)
    a.configure(text=r0)
    if a0.get() == str(r0):
        a.configure(fg='lime')
    else:
        a.configure(fg='red')


a.bind('<Button-1>', b)
root.mainloop()
