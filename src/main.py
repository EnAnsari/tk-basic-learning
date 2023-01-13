from tkinter import *

window = Tk()
# window.title('Blockchain Bank')
# window.minsize(400, 300)
# window.maxsize(600, 450)
# window.geometry('400x300')
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

# Label(window, text='First name:').pack()
# first_name = Entry(window)
# first_name.pack()
# Label(window, text='Last name:').pack()
# last_name = Entry(window)
# last_name.pack()
#
# male_var = IntVar()
# Checkbutton(window, text='male', variable=male_var).pack()
#
# def sign_in():
#     prename = ''
#     if male_var.get() == 1:
#         prename = 'mr'
#     else:
#         prename = 'mrs'
#     lbl.config(text=f'Welcome {prename} {first_name.get()} {last_name.get()}')
#
# sign_in_btn = Button(window, text='sign in', command=sign_in)
# sign_in_btn.pack()
#
# lbl = Label(window)
# lbl.pack()

# Modes = [('male', 'man'), ('female', 'woman'), ('unknown', 'none')]
# var = StringVar()
# var.set('man')
#
# for text, mode in Modes:
#     Radiobutton(window, text=text, variable=var, value=mode, indicatoron=0).pack(anchor=W)

# scale_dim = Scale(window, from_=0, to=100, orient=HORIZONTAL)
# scale_dim.pack()
#
# def push_btn():
#     lbl.config(text=f'value = {scale_dim.get()}')
#
# Button(window, text='get value', command=push_btn).pack()
# lbl = Label(window, fg='green')
# lbl.pack()

# Label(window, text='Welcome to translate of TOEFL\'s result', font=('consolas', 10)).pack()
#
# Label(window, text='\n\nReading score', font=('consolas', 8)).pack()
# reading_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# reading_score.pack()
# Label(window, text='Listening score', font=('consolas', 8)).pack()
# listening_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# listening_score.pack()
# Label(window, text='Speaking score', font=('consolas', 8)).pack()
# speaking_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# speaking_score.pack()
# Label(window, text='Writing score', font=('consolas', 8)).pack()
# writing_score = Scale(window, from_=0, to=30, orient=HORIZONTAL)
# writing_score.pack()
#
# def result():
#     total_score = reading_score.get() + listening_score.get() + speaking_score.get() + writing_score.get()
#     if total_score >= 100:
#         lbl.config(text=f'\nWelcome to USA\nYour total score is {total_score}', fg='green')
#     else:
#         lbl.config(text=f'\nTry again!\nYour total score is {total_score}', fg='red')
#
# Button(window, text='show me Result', bg='yellow', command=result).pack()
# lbl = Label(window)
# lbl.pack()


window.title('simple gui')
window.geometry('400x500')

# text = Text(window)
# text.pack()
#
# def save_text():
#     with open('output.txt', 'w') as f:
#         f.write(text.get(1.0, END))
#
# def load_text():
#     with open('output.txt') as f:
#         data = f.read()
#     text.insert(INSERT, data)
#
# Button(window, text='save', command=save_text).pack()
# Button(window, text='load', command=load_text).pack()

# name = Entry(window)
# name.pack()
#
# def clear_list():
#     list_box.delete(0, END)
#
# def insert_list():
#     list_box.insert(END, name.get())
#
# Button(window, text='add', width=15, fg='green', command=insert_list).pack()
# Button(window, text='clear', width=15, fg='red', command=clear_list).pack()
#
# list_box = Listbox(window)
# list_box.pack()

# list_box = Listbox(window)
# Scrollbar(window, command=list_box.yview).pack(side=RIGHT, fill=BOTH)
# list_box.pack(expand=True, fill=BOTH)
#
# for line in range(200):
#     list_box.insert(END, 'this is line number: {}'.format(line + 1))

# spin = Spinbox(window, from_=0, to=100)
# spin.pack()
#
# def print_number():
#     print(spin.get())
#
# Button(window, text='get', command=print_number).pack()

cw = Canvas(window, width=1000, height=1000)
cw.pack()

cw.create_line(10, 10, 10, 100)
cw.create_line(50, 10, 50, 100, fill='red', dash=(3, 3))
cw.create_rectangle(70, 10, 150, 150, fill='blue', outline='red')
cw.create_oval(190, 10, 260, 300, fill='yellow')
cw.create_arc(10, 200, 150, 300, fill='aqua')
cw.create_polygon([300, 10, 400, 350, 500, 200, 700, 300], fill='pink', outline='blue')
cw.create_text(100, 400, fill='darkblue', font='Times 20 italic bold', text='EnAnsari')
# image_file = PhotoImage(file='C:\\Users\\Mateo\\Pictures\\Screenshots\\Screenshot-1.png')
# cw.create_image(400, 500, image=image_file)


window.mainloop()
