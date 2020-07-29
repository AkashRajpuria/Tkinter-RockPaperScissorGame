from tkinter import *
window= Tk()
one=Label(window,text="one",bg="black")
one.pack()
two=Label(window,text="two",bg="blue")
two.pack(fill=X)
three=Label(window,text="three",bg="green")
three.pack(fill=Y,side=LEFT)

def left(event):
    print("left")
def right(event):
    print("right")
window.bind("<Button-1>",left)
window.bind("<Button-3>",right)

window.mainloop()
