from tkinter import *
window=Tk()
window.resizable(840,550)
window.title('hello')
topframe=Frame(window)
topframe.pack()
bottomframe=Frame(window)
bottomframe.pack(side=BOTTOM)
label1=Label(topframe,text="Username")
label1.grid(row=0,column=0)
entery1=Entry(topframe)
entery1.grid(row=0,column=1)
label2=Label(topframe,text="Select Gender")
label2.grid(row=1,column=0)
radio=Radiobutton(topframe,text=("MALE"),value=1,indicatoron = 0)
radio.grid(row=2,column=0)
radio1=Radiobutton(topframe,text='FEMALE',value=2,indicatoron = 0)
radio1.grid(row=2,column=1)
label3=Label(topframe,text="email id")
label3.grid(row=3,column=0)
label4=Label(topframe,text="password")
label4.grid(row=4,column=0)
label5=Label(topframe,text="re enter password")
label5.grid(row=5,column=0)
entery2=Entry(topframe)
entery2.grid(row=3,column=1)
entery3=Entry(topframe,show="*")
entery3.grid(row=4,column=1)
entery4=Entry(topframe,show="*")
entery4.grid(row=5,column=1)


window.mainloop()