from tkinter import *
import webbrowser
import pyttsx3

root = Tk()
root.resizable(False, False)
root.title('TYPE')
a = Entry(root)
a.pack()


def app(event):
    if a.get().__contains__('fg<blue>'):
        a.delete(0, END)
        a.configure(fg='blue')
    elif a.get().__contains__('fg<red>'):
        a.delete(0, END)
        a.configure(fg='red')
    elif a.get().__contains__('fg<lime>'):
        a.delete(0, END)
        a.configure(fg='lime')
    elif a.get().__contains__('fg<yellow>'):
        a.delete(0, END)
        a.configure(fg='yellow')

    elif a.get().__contains__('bg<red>'):
        a.delete(0, END)
        a.configure(bg='red')
    elif a.get().__contains__('bg<blue>'):
        a.delete(0, END)
        a.configure(bg='blue')
    elif a.get().__contains__('bg<lime>'):
        a.delete(0, END)
        a.configure(bg='lime')
    elif a.get().__contains__('bg<yellow>'):
        a.delete(0, END)
        a.configure(bg='yellow')

    elif a.get().__contains__('<happy>'):
        a.delete(0, END)
        a.insert(0, '😊')
    elif a.get().__contains__('<sad>'):
        a.delete(0, END)
        a.insert(0, '😭')
    elif a.get().__contains__('<angry>'):
        a.delete(0, END)
        a.insert(0, '😡')
    elif a.get().__contains__('<love>'):
        a.delete(0, END)
        a.insert(0, '😍')

    elif a.get().__contains__('<close>'):
        root.destroy()


def fun0(event):
    a.delete(0, END)


def search(event):
    url = "https://www.google.com.tr/search?q={}".format(a.get())
    webbrowser.open(url)
    a.delete(0, END)


def say(event):
    pyttsx3.speak(a.get())
    a.delete(0, END)


root.bind('<Key>', app)
root.bind('<Control-d>', fun0)
root.bind('<Return>', search)
root.bind('<Control-s>', say)
root.mainloop()
