import numpy as np
import matplotlib.pyplot as plt

#Для всех вариантов [a, b] = [0; 1], [c, d] = [0; 10], f(x,t)=0
#Погрешность решения 0,01.

start, time_start = 0, 0 # a = start, c = time_start
end, time_end = 1, 10 # b = end, d = time_end
#т.к. эти буквы использованы для метода прогонки

h = 0.1
time = 0.01 #погрешность

number_h = int((end - start) / h) #шаг
number_time = int((time_end - time_start) / time) #шаг

#функция для того, чтобы инициализировать U
def initialization():
    u = np.zeros((number_time, number_h))
    for i in range(number_h):
        u[0][i] = (i * h)**2 #u(0,x) = x^2
        u[1][i] = u[0][i] + time * (-1) #du/dt(0,x) = -1
    for j in range(number_time):
        u[j][0] = 0  #u(t,0) = 0
        u[j][number_h - 1] = 1 #u(t,1) = 1
    return u

def explicit_method():
    u = initialization()
    lamb = 1 * (time**2) / (h**2)
    for j in range(1, number_time - 1):
        for i in range(1, number_h - 1):
            u[j+1][i] = 2*(1 - lamb) * u[j][i] + lamb*(u[j][i+1] + u[j][i-1]) - u[j-1][i] #формула
    return (u, "Явный метод в виде креста \"+\" ")
    
def implicit_method():
    u = initialization()
    lamb = 1 * (time**2) / (2 * h**2) # D^2 = 1
    alpha, beta, gamma, A, B, C = np.zeros(number_h), np.zeros(number_h), np.zeros(number_h), lamb, (2 * lamb + 1), lamb

    # Метод прогонки
    for j in range(1, number_time - 1):
        alpha[number_h - 1] = 0
        beta[number_h - 1] = u[j+1][number_h - 1]
        gamma[number_h - 1] = 1 / (B - C * alpha[number_h - 1])
        for i in range(number_h -1, 0, -1):
            alpha[i - 1] = gamma[i] * A 
            beta[i - 1] = gamma[i] * (C * beta[i] - (u[j-1][i] - 2 * u[j][i]))
            gamma[i - 1] = 1 / (B - C * alpha[i-1])
        for i in range(number_h - 1):
            u[j+1][i+1] = alpha[i] * u[j+1][i] + beta[i] #та самая формула из теории

    return (u, "Неявный метод в виде \"][\" ")
    
    
def T_implicit_method():
    u = initialization()
    lamb = 1 * (time**2) / (2 * h**2) # D^2 = 1
    a, b, c = np.zeros(number_h), np.zeros(number_h), np.zeros(number_h)

    # Метод прогонки
    for j in range(1, number_time - 1):
        a[number_h - 1] = 0
        b[number_h - 1] = u[j+1][number_h - 1]
        c[number_h - 1] = 1 / (1 + 2*lamb - lamb * a[number_h - 1])
        for i in range(number_h - 2, 0, -1):
            a[i-1] = c[i] * lamb
            b[i-1] = c[i] * (lamb * b[i] - (u[j-1][i] - 2 * u[j][i]))
            c[i-1] = 1 / (1 + 2 * lamb - lamb * a[i-1])
        for i in range(1, number_h - 1):
            u[j+1][i+1] = a[i] * u[j+1][i] + b[i] #та самая формула из теории

    return (u, "Неявный метод в виде \"T\" ")

np.set_printoptions(linewidth=100, precision=6, suppress=True, floatmode="fixed") #чтобы красиво выводились числа в таблице, например 0.0008, а не просто 0
plots_color_theme = "winter" #вот тут менять цвет графика
for (graph, title) in [explicit_method(), implicit_method(), T_implicit_method()]:
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
