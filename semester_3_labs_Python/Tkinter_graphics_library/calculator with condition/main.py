import tkinter as calculator
window=calculator.Tk()
window.geometry('250x50')
window.title('Перевод в другую СС')

Ent1=calculator.Entry(width=20)
Ent1.grid(row=0,column=1)
Ent1.pack()

def mainfunction():
    global Ent1
    a=int(Ent1.get())
    print(f'В 2-ой системе счисления {bin(a)}')
    print(f'В 8-ой системе счисления {oct(a)}')
    print(f'В 16-ой системе счисления {hex(a)}')

Buttons=calculator.Button(window,text='Перевести', font=("Arial",10),command=mainfunction)
Buttons.pack()

window.mainloop()
