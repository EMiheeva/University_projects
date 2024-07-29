import numpy as np
import matplotlib.pyplot as plt

def U(x):
    return 3 if x >= 0.5 else 4

a, c = 0, 0
b, d = 1, 1
epsilon = 0.01

def artificial_viscosity_method():
    I = 10
    J = 1000
    h = (b - a) / I 
    tau = (d - c) / J
    u = np.zeros((J, I + 1))

    for i in range(I):
        u[0][i] = U(a + i * h)

    for j in range(1, J):
        for i in range(I):
            u[j][i] = u[j - 1][i] - (tau / h ) * u[j - 1][i] * (u[j - 1][i] - u[j - 1][i - 1]) - ((tau * epsilon ** 2) / (2 * h ** 3)) * (u[j - 1][i + 1] - u[j - 1][i - 1]) * (u[j - 1][i + 1] - u[j - 1][i] + u[j - 1][i - 1])

    return (u[:, :-1], 'Метод с искусственной вязкостью\n')
    
def conservative_method():
    I = 10
    J = 1000
    h = (b - a) / I 
    tau = (d - c) / J 
    u = np.zeros((J, I + 1))

    for i in range(I):
        u[0][i] = U(a  + i * h)

    for j in range(J - 1):
        for i in range(I):
            u[j + 1][i] = u[j][i] - (tau / (2 * h)) * (u[j][i] * u[j][i] - u[j][i - 1] * u[j][i - 1])

    return (u[:, :-1], 'Консервативная схема\n')

np.set_printoptions(linewidth=100, precision=6, suppress=True, floatmode="fixed")
plots_color_theme = "winter"
for (graph, title) in [artificial_viscosity_method(), conservative_method()]:
    fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})
    plt.title(title)
    ax.set_xlabel("t - время")
    ax.set_ylabel("x - положение")
    ax.set_zlabel("U - решение")
    ax.set_rasterization_zorder(1)
    t, x = np.meshgrid(np.linspace(c, d, 1000), np.linspace(a, b, 10))
    x = x.T
    t = t.T
    print(title,'Двумерная числовая таблица приближенных значений U[i][j]\nU = ', graph)
    ax.plot_surface(t, x, graph, cmap=plots_color_theme)
    ax.grid(True)
plt.show()
