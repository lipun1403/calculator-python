from tkinter import *

window = Tk()

window.geometry('500x500')
window.title("Calculator")

inp = Entry(window, width=35)
inp.place(x=0, y=0)

def click(num):
    result=inp.get()
    inp.delete(0, END)
    inp.insert(0,str(result)+str(num))

def clear():
    inp.delete(0, END)

def equal():
    result=eval(inp.get())
    inp.delete(0, END)
    inp.insert(0,result)

def delete():
    data=inp.get()
    inp.delete(0, END)
    inp.insert(0,data[:-1])



b = Button(window, text='1', height=2, width=5, command=lambda: click(1))
b.place(x=10, y=50)

b = Button(window, text='2', height=2, width=5, command=lambda: click(2))
b.place(x=60, y=50)

b = Button(window, text='3', height=2, width=5, command=lambda: click(3))
b.place(x=110, y=50)

b = Button(window, text='4', height=2, width=5, command=lambda: click(4))
b.place(x=10, y=100)

b = Button(window, text='5', height=2, width=5, command=lambda: click(5))
b.place(x=60, y=100)

b = Button(window, text='6', height=2, width=5, command=lambda: click(6))
b.place(x=110, y=100)

b = Button(window, text='7', height=2, width=5, command=lambda: click(7))
b.place(x=10, y=150)

b = Button(window, text='8', height=2, width=5, command=lambda: click(8))
b.place(x=60, y=150)

b = Button(window, text='9', height=2, width=5, command=lambda: click(9))
b.place(x=110, y=150)

b = Button(window, text='0', height=2, width=5, command=lambda: click(0))
b.place(x=60, y=200)

b = Button(window, text='+', height=2, width=5, command=lambda: click('+'))
b.place(x=160, y=50)

b = Button(window, text='-', height=2, width=5, command=lambda: click('-'))
b.place(x=160, y=100)

b = Button(window, text='*', height=2, width=5, command=lambda: click('*'))
b.place(x=160, y=150)

b = Button(window, text='/', height=2, width=5, command=lambda: click('/'))
b.place(x=160, y=200)

b = Button(window, text='=', height=2, width=5, command=lambda: equal())
b.place(x=110, y=200)

b = Button(window, text='.', height=2, width=5, command=lambda: click('.'))
b.place(x=10, y=200)

b = Button(window, text='clear', height=2, width=5, command=lambda: clear())
b.place(x=10, y=250)

b = Button(window, text='delete', height=2, width=5, command=lambda: delete())
b.place(x=60, y=250)

b = Button(window, text='(', height=2, width=5, command=lambda: click('('))
b.place(x=110, y=250)

b = Button(window, text=')', height=2, width=5, command=lambda: click(')'))
b.place(x=160, y=250)


window.mainloop()