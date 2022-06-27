from tkinter import *
root = Tk()

o = Entry(root)
o.grid(row=0, column=0)


o0 = Label(root, text='')
o0.grid(row=1, column=0)


def d(event):
    if o.get() == '._':
        o0.configure(text=str(o0.cget('text') + 'a'))
    elif o.get() == '_...':
        o0.configure(text=str(o0.cget('text') + 'b'))
    elif o.get() == '_._.':
        o0.configure(text=str(o0.cget('text') + 'c'))
    elif o.get() == '_..':
        o0.configure(text=str(o0.cget('text') + 'd'))
    elif o.get() == '.':
        o0.configure(text=str(o0.cget('text') + 'e'))
    elif o.get() == '.._.':
        o0.configure(text=str(o0.cget('text') + 'f'))
    elif o.get() == '__.':
        o0.configure(text=str(o0.cget('text') + 'g'))
    elif o.get() == '....':
        o0.configure(text=str(o0.cget('text') + 'h'))
    elif o.get() == '..':
        o0.configure(text=str(o0.cget('text') + 'i'))
    elif o.get() == '.___':
        o0.configure(text=str(o0.cget('text') + 'j'))
    elif o.get() == '_._':
        o0.configure(text=str(o0.cget('text') + 'k'))
    elif o.get() == '._..':
        o0.configure(text=str(o0.cget('text') + 'l'))
    elif o.get() == '__':
        o0.configure(text=str(o0.cget('text') + 'm'))
    elif o.get() == '_.':
        o0.configure(text=str(o0.cget('text') + 'n'))
    elif o.get() == '___':
        o0.configure(text=str(o0.cget('text') + 'o'))
    elif o.get() == '.__.':
        o0.configure(text=str(o0.cget('text') + 'p'))
    elif o.get() == '__._':
        o0.configure(text=str(o0.cget('text') + 'q'))
    elif o.get() == '._.':
        o0.configure(text=str(o0.cget('text') + 'r'))
    elif o.get() == '...':
        o0.configure(text=str(o0.cget('text') + 's'))
    elif o.get() == '_':
        o0.configure(text=str(o0.cget('text') + 't'))
    elif o.get() == '.._':
        o0.configure(text=str(o0.cget('text') + 'u'))
    elif o.get() == '..._':
        o0.configure(text=str(o0.cget('text') + 'v'))
    elif o.get() == '.__':
        o0.configure(text=str(o0.cget('text') + 'w'))
    elif o.get() == '_.._':
        o0.configure(text=str(o0.cget('text') + 'x'))
    elif o.get() == '_.__':
        o0.configure(text=str(o0.cget('text') + 'y'))
    elif o.get() == '__..':
        o0.configure(text=str(o0.cget('text') + 'z'))

    if o.get() == 'a':
        o0.configure(text=str(o0.cget('text') + '._'))
    elif o.get() == 'b':
        o0.configure(text=str(o0.cget('text') + '_...'))
    elif o.get() == 'c':
        o0.configure(text=str(o0.cget('text') + '_._.'))
    elif o.get() == 'd':
        o0.configure(text=str(o0.cget('text') + '_..'))
    elif o.get() == 'e':
        o0.configure(text=str(o0.cget('text') + '.'))
    elif o.get() == 'f':
        o0.configure(text=str(o0.cget('text') + '.._.'))
    elif o.get() == 'g':
        o0.configure(text=str(o0.cget('text') + '__.'))
    elif o.get() == 'h':
        o0.configure(text=str(o0.cget('text') + '....'))
    elif o.get() == 'i':
        o0.configure(text=str(o0.cget('text') + '..'))
    elif o.get() == 'j':
        o0.configure(text=str(o0.cget('text') + '.___'))
    elif o.get() == 'k':
        o0.configure(text=str(o0.cget('text') + '_._'))
    elif o.get() == 'l':
        o0.configure(text=str(o0.cget('text') + '._..'))
    elif o.get() == 'm':
        o0.configure(text=str(o0.cget('text') + '__'))
    elif o.get() == 'n':
        o0.configure(text=str(o0.cget('text') + '_.'))
    elif o.get() == 'o':
        o0.configure(text=str(o0.cget('text') + '___'))
    elif o.get() == 'p':
        o0.configure(text=str(o0.cget('text') + '.__.'))
    elif o.get() == 'q':
        o0.configure(text=str(o0.cget('text') + '__._'))
    elif o.get() == 'r':
        o0.configure(text=str(o0.cget('text') + '._.'))
    elif o.get() == 's':
        o0.configure(text=str(o0.cget('text') + '...'))
    elif o.get() == 't':
        o0.configure(text=str(o0.cget('text') + '_'))
    elif o.get() == 'u':
        o0.configure(text=str(o0.cget('text') + '.._.'))
    elif o.get() == 'v':
        o0.configure(text=str(o0.cget('text') + '..._'))
    elif o.get() == 'w':
        o0.configure(text=str(o0.cget('text') + '.__'))
    elif o.get() == 'x':
        o0.configure(text=str(o0.cget('text') + '_.._'))
    elif o.get() == 'y':
        o0.configure(text=str(o0.cget('text') + '_.__'))
    elif o.get() == 'z':
        o0.configure(text=str(o0.cget('text') + '__..'))


def d0(event):
    o0.configure(text='')


root.bind('<Return>', d)
o0.bind('<Button-1>', d0)
root.mainloop()
