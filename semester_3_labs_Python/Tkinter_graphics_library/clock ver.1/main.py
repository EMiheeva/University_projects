import tkinter as tk
import datetime
import math


def draw():
    c.delete('all')
    c.create_oval(10,10,410,410, width=3)

    dt=datetime.datetime.now()

    R_hour=140
    R_minutes=180
    R_seconds=180

    angle_seconds=dt.second/30*math.pi
    x_end=210+R_seconds*math.sin(angle_seconds)
    y_end=210-R_seconds*math.cos(angle_seconds)
    c.create_line(210,210,x_end,y_end, width=1, fill='red')
    angle_minutes=dt.minute/30*math.pi+angle_seconds/60
    x_end=210+R_minutes*math.sin(angle_minutes)
    y_end=210-R_minutes*math.cos(angle_minutes)
    c.create_line(210,210,x_end,y_end, width=1)
    angle_hour=dt.hour/6*math.pi+angle_minutes/60
    x_end=210+R_hour*math.sin(angle_hour)
    y_end=210-R_hour*math.cos(angle_hour)
    c.create_line(210,210,x_end,y_end, width=3)

    c.create_text(210,430,tex=dt, font='Verdana 16')
    root.after(1000, draw)

    numbers = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]

    for i in range(0, len(numbers)):        
        c.create_text(
            210 - 160 * math.sin(((i+1)*2*math.pi)/12), 
            210 - 160 * math.cos(((i+1)*2*math.pi)/12), 
            text=numbers[i], 
            font=('Arial',12, 'bold'), 
            fill='black'
        )
    
    

root=tk.Tk()
root.title('Часы')

c=tk.Canvas(width=420, height=450, bg='white')
c.pack()

draw()

root.mainloop()
