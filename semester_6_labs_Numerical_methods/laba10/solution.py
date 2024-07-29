import numpy as np
import matplotlib.pyplot as plt

#Для всех вариантов [a, b] = [0; 10], [c, d] = [0; 10]. Погрешность решения 0,01.
epsilon = 0.01
start, time_start = 0, 0 # a = start, c = time_start
end, time_end = 10, 10 # b = end, d = time_end


#Если у тебя есть идеи, как это оптимизировать, то придумай
#Для всех вариантов граничные условия U(x,c)=x+c, U(x,d)=x+d, U(a,y)=a+y, U(b,y)=b+y
def f(x, y):
    return x * y ** 2
def u_a_y(y):
    return start + y
def u_b_y(y):
    return end + y
def u_x_c(x):
    return x + time_start
def u_x_d(x):
    return x + time_end
    
#метод зейделя - это мидифицированный метод итераций, когда в правой части уже посчитаны значения
def method_seidel(seidel, size_for_grid, h, x, y, u):
            u_prev = u.copy() if not seidel else None
            for i in range(1, size_for_grid - 1):
                for j in range(1, size_for_grid - 1):
                    if seidel:
                        u[i, j] = (u[i + 1, j] + u[i - 1,j] + u[i, j + 1] + u[i, j - 1]) / 4 + (h**2) * f(x[i], y[j])
                    else:
                        u[i, j] = (u_prev[i + 1, j] + u_prev[i - 1,j] + u_prev[i, j + 1] + u_prev[i, j - 1]) / 4 + (h**2) * f(x[i], y[j])
            return u
            
def method_iteration(seidel, h, x, y):
            number_h = (end - start) / (h - 1)
            u = np.zeros(shape=(h, h), dtype=float)

            u[0, :] = u_a_y(y)
            u[:, 0] = u_x_c(x)
            u[-1, :] = u_b_y(y)
            u[:, -1] = u_x_d(x)

            u1 = method_seidel(seidel, h, number_h, x, y, u.copy())
            iteration = 1
            while np.max(np.abs(u - u1)) > epsilon:
                u = u1 
                u1 = method_seidel(seidel, h, number_h, x, y, u.copy())
                iteration += 1

            return u1, iteration

#Сама придумала такой способ ввода с клавиатуры 5 или 10 и вводить выбор метода
def get_user_input():
    grid_size = int(input("Введите размер сетки (5/10): "))
    seidel_input = input("Хотите использовать метод Зейделя? (да/нет): ")
    seidel = True if seidel_input.lower() == 'да' else False
    return grid_size, seidel

size_for_grid, seidel = get_user_input()
plots_color_theme = "winter"
np.set_printoptions(linewidth=100, precision=6, suppress=True, floatmode="fixed")#чтобы были красивые числа в матрице
#grid_size = 10
#grid_size = 5
#seidel = True
#seidel = False

x = np.linspace(start, end, size_for_grid)
y = np.linspace(time_start, time_end, size_for_grid)
u, k = method_iteration(seidel, size_for_grid, x, y)

title = f"Метод {'Зейделя' if seidel else 'простой итерации'} с размером сетки {size_for_grid}x{size_for_grid} (итераций: {k})"
print(title)
print(f"Двумерная числовая таблица значений U[i][j]\nU = {u}")
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(x, y)
ax.plot_surface(X.T, Y.T, u, cmap=plots_color_theme)
ax.set_title(title)
ax.set_xlabel("t - время")
ax.set_ylabel("x - положение")
ax.set_zlabel("U(x,t) - решение")
ax.set_xlim(start, end)
ax.set_ylim(time_start, time_end)
plt.show()
