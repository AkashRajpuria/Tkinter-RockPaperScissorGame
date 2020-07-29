from tkinter import *
window= Tk()
def printname(event):
    print("Hello HUi")
button1=Button(window,text="Click me")
button1.bind("<Button>",printname)
button1.pack()
window.mainloop()
