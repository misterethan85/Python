import tkinter
import math

x = ''
y = ''
op = ''

def calc(a):
    global x,y,op
    if a == 'C':
        entry.delete(0,len(entry.get()))

    elif a in '+-*/':
        op = a
        x = entry.get()
        entry.delete(0,len(x))
        print(x)
    elif a == 'x^2':
        y = float(entry.get())
        op = math.sqrt(y)
        entry.delete(0,25)
        entry.insert(0,str(op))
    elif a == '=':
        y = entry.get()
        entry.delete(0,len(entry.get()))
        entry.insert(0,str(eval(x+op+y)))
    else:
        entry.insert(len(entry.get()),a)

    
window = tkinter.Tk()
window.wm_title('calculator')
entry = tkinter.Entry(window)
entry.pack()
frame = tkinter.Frame(window)
frame.pack()

button0 = tkinter.Button(frame,text= 'C',fg='red',font=('Courier','14','bold'),
                         command =lambda: calc('C'))
button0.config(height=6,width=2)
button0.grid(rowspan=5,column=6)
button1 = tkinter.Button(frame,text='1',font=('Courier','14'),
                         command=lambda: calc('1'))
button1.grid(row=3,column=0)
button2 = tkinter.Button(frame,text='2',font=('Courier','14'),
                         command=lambda: calc('2'))
button2.grid(row=3,column=1)
button3 = tkinter.Button(frame,text='3',font=('Courier','14'),
                         command=lambda: calc('3'))
button3.grid(row=3,column=2)
button4 = tkinter.Button(frame,text='4',font=('Courier','14'),
                         command=lambda: calc('4'))
button4.grid(row=2,column=0)
button5 = tkinter.Button(frame,text='5',font=('Courier','14'),
                         command=lambda: calc('5'))
button5.grid(row=2,column=1)
button6 = tkinter.Button(frame,text='6',font=('Courier','14'),
                         command=lambda: calc('6'))
button6.grid(row=2,column=2)
button7 = tkinter.Button(frame,text='7',font=('Courier','14'),
                         command=lambda: calc('7'))
button7.grid(row=1,column=0)
button8 = tkinter.Button(frame,text='8',font=('Courier','14'),
                         command=lambda: calc('8'))
button8.grid(row=1,column=1)
button9 = tkinter.Button(frame,text='9',font=('Courier','14'),
                         command=lambda: calc('9'))
button9.grid(row=1,column=2)
button10 = tkinter.Button(frame,text='0',font=('Courier','14'),
                         command=lambda: calc('0'))
button10.grid(row=4,column=1)
button11 = tkinter.Button(frame,text='+',font=('Courier','14'),
                         command=lambda: calc('+'))
button11.grid(row=1,column=3)
button12 = tkinter.Button(frame,text='-',font=('Courier','14'),
                         command=lambda: calc('-'))
button12.grid(row=2,column=3)
button13 = tkinter.Button(frame,text='*',font=('Courier','14'),
                         command=lambda: calc('*'))
button13.grid(row=3,column=3)
button14 = tkinter.Button(frame,text=chr(247),font=('Courier','14'),
                         command=lambda: calc('/'))
button14.grid(row=4,column=3)
button15 = tkinter.Button(frame,text='=',fg='blue',font=('Courier','14'),
                         command=lambda: calc('='))
button15.grid(row=4,column=2)
button16 = tkinter.Button(frame,text='.',font=('Courier','14'),
                         command=lambda: calc('.'))
button16.grid(row=4,column=0)
button17 = tkinter.Button(frame,text='x^2',font=('Courier','14'),
                         command=lambda: calc('x^2'))
button17.grid(row=1,column=5)
button18 = tkinter.Button(frame,text='TBA',font=('Courier','14'),
                         command=lambda: calc('TBA'))
button18.grid(row=2,column=5)
button19 = tkinter.Button(frame,text='TBA',font=('Courier','14'),
                         command=lambda: calc('TBA'))
button19.grid(row=3,column=5)
button20 = tkinter.Button(frame,text='TBA',font=('Courier','14'),
                         command=lambda: calc('TBA'))
button20.grid(row=4,column=5)
window.mainloop()
