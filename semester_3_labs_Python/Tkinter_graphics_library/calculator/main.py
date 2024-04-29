import tkinter as calc
window=calc.Tk()
window.title('Калькулятор')


textEntry = calc.StringVar()
Ent1 = calc.Entry(width=20,  textvariable = textEntry)
Ent1.grid(row=0, column=0, columnspan=3)

def plus1():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number+1)
    except ValueError:
        print("Введите число")

def plus2():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number+2)
    except ValueError:
        print("Введите число")

def plus3():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number+3)
    except ValueError:
        print("Введите число")

def minus1():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number-1)
    except ValueError:
        print("Введите число")

def minus2():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number-2)
    except ValueError:
        print("Ошибка! Введите число")

def minus3():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number-3)
    except ValueError:
        print("Введите число")

def multiply2():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number*2)
    except ValueError:
        print("Ошибка! Введите число")

def multiply3():
    global Ent1, textEntry
    try:
        number = int(Ent1.get())
        textEntry.set(number*3)
    except ValueError:
        print("Введите число")

def Del():
    Ent1.delete(0, 'end')
 
Button1=calc.Button(window,text='+1', font=("Arial",10),command=lambda:plus1()).grid(row=1,column=0)
Button2=calc.Button(window,text='+2', font=("Arial",10),command=lambda:plus2()).grid(row=1, column=1)
Button3=calc.Button(window,text='+3', font=("Arial",10),command=lambda:plus3()).grid(row=1, column=2)
Button4=calc.Button(window,text='- 1', font=("Arial",10),command=lambda:minus1()).grid(row=2, column=0)
Button5=calc.Button(window,text='- 2', font=("Arial",10),command=lambda:minus2()).grid(row=2, column=1)
Button6=calc.Button(window,text='- 3', font=("Arial",10),command=lambda:minus3()).grid(row=2, column=2)
Button7=calc.Button(window,text='* 2', font=("Arial",10),command=lambda:multiply2()).grid(row=3, column=0)
Button8=calc.Button(window,text='* 3', font=("Arial",10),command=lambda:multiply3()).grid(row=3, column=1)
Button9=calc.Button(window,text='= 0', font=("Arial",10),command=Del).grid(row=3, column=2)

window.mainloop()
