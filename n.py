# -*- coding: utf-8 -*-
from tkinter import *
from math import *

root=Tk()
root.title('Калькулятор')

e= StringVar()


def res():
    a= eval(e.get())
    ent.delete(0,23) #для равно фунция
    ent.insert(0,a)

def b1():
    ent.insertbackground (1)


ent = Entry(root,width=20,bd=3,textvariable=e)
bt1=Button(root, width=20,height=3,text='1',command=b1)
bt2=Button(root, width=20,height=3,text='2')
bt3=Button(root, width=20,height=3,text='3')
bt4=Button(root, width=20,height=3,text='4')
bt5=Button(root, width=20,height=3,text='5')
bt6=Button(root, width=20,height=3,text='6')
bt7=Button(root, width=20,height=3,text='7')
bt8=Button(root, width=20,height=3,text='8')
bt9=Button(root, width=20,height=3,text='9')
btplus=Button(root, width=20,height=3,text='+')
btmin=Button(root, width=20,height=3,text='-')
btdel=Button(root, width=20,height=3,text='/')
btumn=Button(root, width=20,height=3,text='*')
btres=Button(root, width=20,height=3,text='=',command=res)

ent.grid(row = 4, column = 1)
bt1.grid(row = 1, column = 1)
bt2.grid(row = 1, column = 2)
bt3.grid(row = 1, column = 3)
bt4.grid(row = 2, column = 1)
bt5.grid(row = 2, column = 2)
bt6.grid(row = 2, column = 3)
bt7.grid(row = 3, column = 1)
bt8.grid(row = 3, column = 2)
bt9.grid(row = 3, column = 3)
btplus.grid(row = 1, column = 4)
btmin.grid(row = 1, column = 5)
btdel.grid(row = 2, column = 4)
btumn.grid(row = 2, column = 5)
btres.grid(row = 3, column = 4)






root.mainloop()


