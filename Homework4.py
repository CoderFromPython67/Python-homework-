
from tkinter import *
from datetime import date

root = Tk()
root.title('Homework thing')
root.geometry('400x300')

lbl = Label(text="Hey There!", fg="white", bg="#1F61B1", height=1, width=300)

name_lbl = Label(text="Full Name", bg="#07578D")
name_entry = Entry()


def display():	
	name = name_entry.get()	
	global message
	message = "Hello there! \nToday's date is: "
	greet = "Hello "+name+"\n"
	
	text_box.insert(END, greet)
	text_box.insert(END, message)
	text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="#46AC42", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
