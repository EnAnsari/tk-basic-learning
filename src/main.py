from tkinter import *

window = Tk()
window.title('Blockchain Bank')
window.minsize(400, 300)
window.maxsize(600, 450)
window.geometry('400x300')
# window.resizable(width=False, height=False)

# Label(window, text='Hello World!').pack()
# Label(window, text='Hello World!', font=('Tahoma', 20)).pack()
# Label(window, text='Hello World!', background='aqua', foreground='blue').pack()
#
# Button(window, text='click me!', bg='yellow').pack()

# hello_label = Label(window, text='hello world')
# hello_label.pack()
#
# hello_label.config(fg='blue')

# def print_hello():
#     print('hello world!')
#
# btn = Button(window, text='click me!', command=print_hello)
# btn.pack()

# counter = 0
#
# def increse_counter():
#     global counter
#     counter += 1
#     # print(counter)
#     lbl.config(text=f'counter = {counter}')
#
# btn = Button(window, text='click me!', command=increse_counter)
# lbl = Label(window, text='counter = 0')
#
# lbl.pack()
# btn.pack()

# def change_status():
#     lbl.config(text='status: online', foreground='green')
#
# btn = Button(window, text='click me!', command=change_status, width=40, border=5)
# lbl = Label(window, text='status: offline', fg='red')
#
# lbl.pack()
# btn.pack()

Label(window, text='First name:').pack()
first_name = Entry(window)
first_name.pack()
Label(window, text='Last name:').pack()
last_name = Entry(window)
last_name.pack()

def sign_in():
    lbl.config(text=f'Welcome mr/mrs {first_name.get()} {last_name.get()}')

sign_in_btn = Button(window, text='sign in', command=sign_in)
sign_in_btn.pack()

lbl = Label(window)
lbl.pack()

window.mainloop()
