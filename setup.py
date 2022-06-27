from tkinter import *
from tkinter import messagebox
root = Tk()
i = input(' If You Signed In write : SignIn \n'
          'If You Wanna SignUp write : SignUp >')
i0 = open('lol.txt', 'a')
if i == 'SignIn':
    pass
elif i == 'SignUp':
    try:
       i0.truncate(0)
       o = input(' Pass >')
       i0.write(str(o))
       i0.close()
    except Exception:
        pass


a0 = Label(root, width=3, height=2, bg='gray')
a0.place(x=0, y=0)

a1 = Label(root, width=3, height=2, bg='gray')
a1.place(x=40, y=0)

a2 = Label(root, width=3, height=2, bg='gray')
a2.place(x=80, y=0)

a3 = Label(root, width=3, height=2, bg='gray')
a3.place(x=120, y=0)


def app():
    def b0(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='0')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='0')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='0')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='0')
                        app()
                    else:
                        app()
                        pass

    def b1(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='1')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='1')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='1')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='1')
                        app()
                    else:
                        app()
                        pass

    def b2(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='2')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='2')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='2')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='2')
                        app()
                    else:
                        app()
                        pass

    def b3(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='3')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='3')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='3')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='3')
                        app()
                    else:
                        app()
                        pass

    def b4(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='4')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='4')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='4')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='4')
                        app()
                    else:
                        app()
                        pass

    def b5(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='5')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='5')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='5')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='5')
                        app()
                    else:
                        app()
                        pass

    def b6(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='6')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='6')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='6')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='6')
                        app()
                    else:
                        app()
                        pass

    def b7(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='7')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='7')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='7')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='7')
                        app()
                    else:
                        app()
                        pass

    def b8(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='8')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='8')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='8')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='8')
                        app()
                    else:
                        app()
                        pass

    def b9(event):
        global a0, a1, a2, a3
        if a0.cget('text') == '':
            a0.configure(text='9')
            app()
        else:
            if a1.cget('text') == '':
                a1.configure(text='9')
                app()
            else:
                if a2.cget('text') == '':
                    a2.configure(text='9')
                    app()
                else:
                    if a3.cget('text') == '':
                        a3.configure(text='9')
                        app()
                    else:
                        pass

    def enter(event):
        with open('lol.txt') as f:
            c = f.read()

        passs = str(a0.cget('text')) + str(a1.cget('text')) + str(a2.cget('text')) + str(a3.cget('text'))
        if str(passs) == str(c):
            messagebox.showinfo('Info', 'Login Success')
            root.destroy()
        else:
            messagebox.showinfo('Info', 'Wrong Input')
            a0.configure(text='')
            a1.configure(text='')
            a2.configure(text='')
            a3.configure(text='')
            app()

    root.bind('<Key-0>', b0)
    root.bind('<Key-1>', b1)
    root.bind('<Key-2>', b2)
    root.bind('<Key-3>', b3)
    root.bind('<Key-4>', b4)
    root.bind('<Key-5>', b5)
    root.bind('<Key-6>', b6)
    root.bind('<Key-7>', b7)
    root.bind('<Key-8>', b8)
    root.bind('<Key-9>', b9)
    root.bind('<Return>', enter)


app()
root.mainloop()
