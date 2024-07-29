import numpy as np
import matplotlib.pyplot as plt

#Для всех вариантов [a, b] = [0; 1], [c, d] = [0; 10], D=1. Погрешность решения 0,01.

start, time_start = 0, 0 # a = start, c = time_start
end, time_end = 1, 10 # b = end, d = time_end
#т.к. эти буквы использованы для метода прогонки

h = 0.1
time = 0.005

number_h = int((end - start) / h) #шаг
number_time = int((time_end - time_start) / time) #шаг
lamb = 1 * time / (h**2) # D^2 = 1

# инициализируем u с помощью функции
def initialization():
    u = np.zeros((number_time, number_h))
    for i in range(number_h):
        u[0][i] = (i * h)**3 #u(0,x) = x^3
    for j in range(number_time):
        u[j][0] = 0  #u(t,0) = 0
        u[j][number_h - 1] = 1 #u(t,1) = 1
    return u
    
def explicit_method():
    u = initialization()
    for j in range(number_time - 1):
        for i in range(1, number_h - 1):
            u[j+1][i] = (u[j][i + 1] + u[j][i-1])/2 #формула
    return (u, "Явный метод в виде перевернутой \"Т\" ")
    
def implicit_method():
    u = initialization()
    
    #Метод прогонки
    a, b, c = np.zeros(number_h), np.zeros(number_h), np.zeros(number_h)
    A = lamb 
    B = lamb * 2 + 1
    for j in range(0, number_time - 1):
        a[number_h - 1] = 0
        b[number_h - 1] = u[j + 1][number_h - 1]
        c[number_h - 1] = 1 / (B - A * a[number_h - 1])
        for i in range(number_h - 1, 0, -1):
            a[i - 1] = c[i] * A
            b[i - 1] = c[i] * (A * b[i] + u[j][i])
            c[i - 1] = 1 / (B - A * a[i - 1])
        for i in range(0, number_h - 1):
            u[j + 1][i + 1] = a[i] * u[j][i] + b[i] #формула
    return (u, "Неявный метод в виде \"T\" ")
    

np.set_printoptions(linewidth=100, precision=6, suppress=True, floatmode="fixed") #чтобы красивые были числа в матрице в ответе
plots_color_theme = "winter" #вот тут менять цвет графика
for (graph, title) in [explicit_method(), implicit_method()]:
    print(title, "\nДвумерная числовая таблица значений U[i][j]\nU = ", graph)
    X, T = np.meshgrid(np.arange(start, end, h), np.arange(time_start, time_end, time))
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    plt.title(title)
    ax.set_xlabel("t - время")
    ax.set_ylabel("x - положение")
    ax.set_zlabel("U(x,t) - решение")
    surf = ax.plot_surface(X, T, graph, cmap=plots_color_theme, linewidth=0, antialiased=False)
    ax.grid(True)
plt.show()
