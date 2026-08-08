from tkinter import *

root = Tk()
root.geometry('100x100')
root.title('button test')

def handle_keypress(event):
    """click on the printed character associated with the key pressed"""
    print(event.char)

root.bind("<Key>", handle_keypress)

def click(event):
    print("\n button clicked!")

btn = Button(text="Click me!")
btn.pack()

btn.bind("<Button-1>", click)
root.mainloop()

