from tkinter import *
from random import randint
#from PIL import ImageTk,Image
global cp,py,player
cp=0
py=0
player='Anonymous'
def username():
    global player
    
    player=entry.get()
    print (player)
def computer(obj):
    global comp
    #global player
    players=obj
    lbl2=Label(window,width='100')
    lbl2.grid(row=6,column=0)
    select=randint(1,3)
    if select==1:
        comps='Rock'
    elif select==2:
        comps='Paper'
    elif select==3:
        comps='Sissor'
    lbl2.configure(text=" Computer has selected "+comps+ " and " +str(player)+" have selected "+obj,font=("Classic",10))
    if comps==obj:
        lbl5.configure(text='DRAW',font=("Classic",50))
    elif comps=='Paper' and obj=='Rock':
        lbl5.configure(text='Computer Wins',font=("Classic",50))
    elif comps=='Rock' and obj=='Sissor':
        lbl5.configure(text='Computer Wins',font=("Classic",50))
    elif comps=='Sissor' and obj=='Paper':
        lbl5.configure(text='Computer Wins',font=("Classic",50))
    elif comps=='Paper' and obj=='Sissor':
        lbl5.configure(text=str(player)+' Wins',font=("Classic",50))
    elif comps=='Sissor' and obj=='Rock':
        lbl5.configure(text=str(player)+' Wins',font=("Classic",50))
    elif comps=='Rock' and obj=='Paper':
        lbl5.configure(text=str(player)+' Wins',font=("Classic",50))
    global cp,py
    if lbl5.cget('text')=='Computer Wins':
        cp+=1
    elif lbl5.cget('text')==str(player)+' Wins':
        py+=1
    
        
def result():
    lbl8=Label(window,text="")
    lbl8.grid(row=9,column=0)
    lbl8.configure(text="computer score is "+str(cp) +" and " + str(player)+" Score is "+str(py))
    if int(cp)>int(py):
        lbl9=Label(window,text="")
        lbl9.grid(row=10,column=0)
        lbl9.configure(text='Computer is Winner')
    elif int(cp)<int(py):
        lbl9=Label(window,text="")
        lbl9.grid(row=10,column=0)
        lbl9.configure(text=str(player)+' is Winner')
    else:
        lbl9=Label(window,text="")
        lbl9.grid(row=10,column=0)
        lbl9.configure(text='This is a Draw')
        






window=Tk()
window.title("ROck,Paper,Stone")


lbl5=Label(window,text="",font=("Classic",50))
lbl5.grid(row=7,column=1)
lbl=Label(window,text="Username")
lbl.grid(row=0,column=0)
entry=Entry(window)
entry.grid(row=0,column=1)

lbl1=Label(window,text="WELCOME "+entry.get(),font=('Classic',50))
lbl1.grid(row=1,column=0)

btn1=Button(window,text="Computer",width='23',height='15')
btn1.grid(row=3,column=0)

#btn2=Label(window,text="Player",width='23',height='15')
#btn2.grid(row=3,column=1)

btn3=Button(window,text="Rock",width='8',height='2',command=lambda:computer('Rock'))
btn3.grid(row=2,column=1)

btn4=Button(window,text="Paper",width='8',height='2',command=lambda:computer('Paper'))
btn4.grid(row=4,column=1)

btn5=Button(window,text="Sissor",width='8',height='2',command=lambda:computer('Sissor'))
btn5.grid(row=3,column=1)


btn6=Button(window,text='Result',command=result)
btn6.grid(row=8,column=1)

btn8=Button(window,text='Submit',command=username)
btn8.grid(row=0,column=2)



window.mainloop()
