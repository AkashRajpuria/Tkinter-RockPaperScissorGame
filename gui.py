from tkinter import *
window=Tk()
window.title("First gui")
lbl=Label(window,text="Welcome to GUI",font=('Classic',50))
lbl.grid(row=0,column=1)
#lbl.pack()
window.geometry('850x200')
def clicked():#function for performing action when button is clicked
    lbl_1=Label(window)#adding label
    lbl_1.grid(row=3,column=0)#setting label
    lbl_1.configure(text="Button was clicked and we got "+entry.get())#to get the text on entry box
###BUTTON############
btn=Button(window,text='Click me',fg='Yellow',bg='Black',command=clicked)#to get aquainted when button is pressed
btn.grid(row=9,column=1)#setting the button
lbl1=Label(window,text="Username")
lbl2=Label(window,text="Password")
lbl1.grid(row=5,column=0)
lbl2.grid(row=6,column=0)
entry=Entry(window)#to create a empty text box
entry.grid(row=5,column=1)
entry1=Entry(window,state='disabled')#to disable the entry box
entry1.grid(row=6,column=1)
entry1.focus()# to keep the cusor with it

window.mainloop()



