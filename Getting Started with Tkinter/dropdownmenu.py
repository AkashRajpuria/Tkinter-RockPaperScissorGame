from tkinter import *
def donothing():
    print("ok ok")
window=Tk()
menu=Menu(window)
window.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New File",command=donothing)
submenu.add_command(label="New",command=donothing)
submenu.add_separator()
submenu.add_command(label="Exit",command=donothing)

editmenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo",command=donothing)

window.mainloop()
