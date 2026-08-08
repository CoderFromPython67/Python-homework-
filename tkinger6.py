from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('virus detection')
root.geometry('200x200')

def msg():
    messagebox.showwarning("Alert!", "Stop! Malware has been found on your device.")

btn = Button(root, text="Scan for malware?", command=msg)

btn.place(x=40, y=80)
btn.pack()

root.mainloop()