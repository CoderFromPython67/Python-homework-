from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('login app')


frame = Frame(master=root, height=200, width=360, bg="#d0efff")

lbl1 = Label(frame, text='Full name', bg="#10648f", fg="white", width=12)
lbl2 = Label(frame, text='Email id', bg="#10648f", fg="white", width=12)
lbl3 = Label(frame, text='Full password', bg="#10648f", fg="white", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "Hey! "+name
    message = "\n congratulations on your first account!"
    text_box.insert(END, greet)
    text_box.insert(END, message)

text_box = Text(bg="#BEBEBE", fg="black")
btn = Button(text="Create account", command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
text_box.place(y=250)

root.mainloop()

