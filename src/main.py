from tkinter import *

window = Tk()
window.title('Blockchain Bank')
window.minsize(400, 300)
window.maxsize(600, 450)
window.geometry('400x300')
# window.resizable(width=False, height=False)

Label(window, text='Hello World!').pack()
Label(window, text='Hello World!', font=('Tahoma', 20)).pack()
Label(window, text='Hello World!', background='aqua', foreground='blue').pack()

Button(window, text='click me!', bg='yellow').pack()

window.mainloop()
