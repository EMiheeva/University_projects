'''
Численное решение уравнения переноса в прямоугольной области и в полуплоскости
'''
from typing import Callable, Optional
import numpy as np
import matplotlib.pyplot as plt

fun_f = lambda x,t: x
fun_u_x_0 = lambda x: x**2 - 5*x + 5
fun_u_0_x= lambda t: t**2 - 5*t + 5
fun_u_1_x = lambda t: t**2 - 5*t + 1


def solve(
    title: str,   
    I: int,   
    x_start: float,   
    x_end: float,   
    J: int,   
    t_start: float,   
    t_end: float,   
    a: float,   
    fun_f: Callable[[float, float], float],
    fun_u_x_0: Callable[[float], float],
    fun_u_0_x: Optional[Callable[[float], float]],
    fun_u_1_x: Optional[Callable[[float], float]],
    scheme: Callable,):

    lam = a * r / h
    x: list[float] = [x_start + i * h for i in range(I)]   
    t: list[float] = [t_start + j * r for j in range(J)]   
    u: list[list[Optional[float]]] = [[None for _ in range(J)] for _ in range(I)]

    for i in range(I):
        u[i][0] = fun_u_x_0(x[i])
    
    for j in range(J):       
        if fun_u_0_x is not None:           
            u[0][j] = fun_u_0_x(t[j])       
        if fun_u_1_x is not None:           
            u[-1][j] = fun_u_1_x(t[j])   
            
    # Применение схемы
    scheme(u, a, I, x, J, t, lam, fun_f)
    
    # Вывод графика и таблицы
    i_plot_start = None
    i_plot_end = None   
    for i in range(I):
        if abs(x[i] - def_x_start) < 10 ** -6:           
            i_plot_start = i       
        if abs(x[i] - def_x_end) < 10 ** -6:           
            i_plot_end = i   
            
    x_plot = [x[i] for i in range(i_plot_start, i_plot_end + 1)]   
    t_plot = t   
    u_plot = np.array([u[i] for i in range(i_plot_start, i_plot_end + 1)])   
    
    print(title)   
    print(u_plot)   
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    X, T = np.meshgrid(x_plot, t_plot)   
    ax.plot_surface(X.T, T.T, u_plot, cmap=plots_color_theme)
    ax.set_title(title)   
    ax.set_xlabel("x")   
    ax.set_ylabel("t")   
    ax.set_zlabel("u(x,t)")   
    ax.set_xlim(def_x_start, def_x_end)   
    ax.set_ylim(def_t_start, def_t_end)   

    plt.show()


# Схема 1 для [полуплоскости][half]. a > 0
def scheme_1_halfplane_a_pos(u, a, I, x, J, t, lam, fun_f):   
    for j in range(J - 1):       
        for i in range(j + 1, I):
            u[i][j + 1] = lam * u[i - 1][j] + (1 - lam) * u[i][j] + r * fun_f(x[i], t[j])
            
# Схема 1 для [прямоугольной][rect]области. a > 0
def scheme_1_rect_a_pos(u, a, I, x, J, t, lam, fun_f):
    for j in range(J - 1):       
        for i in range(0 + 1, I):
            u[i][j + 1] = lam * u[i - 1][j] + (1 - lam) * u[i][j] + r * fun_f(x[i], t[j])

# Схема 2 для [полуплоскости][half]. a < 0
def scheme_2_halfplane_a_neg(u, a, I, x, J, t, lam, fun_f):   
    for j in range(J - 1):       
        for i in range(I - j - 1): # a<0 обратный порядок
            u[i][j + 1] = -lam * u[i + 1][j] + (1 + lam) * u[i][j] + r * fun_f(x[i], t[j])

# Схема 2 для [прямоугольной][rect]области. a < 0
def scheme_2_rect_a_neg(u, a, I, x, J, t, lam, fun_f):   
    for j in range(J - 1):       
        for i in range(I - 0 - 1): # a<0 обратный порядок
            u[i][j + 1] = -lam * u[i + 1][j] + (1 + lam) * u[i][j] + r * fun_f(x[i], t[j])
            
# Схема 3 для[прямоугольной][rect]области. a > 0
def scheme_3_rect_a_pos(u, a, I, x, J, t, lam, fun_f):   
    for j in range(J - 1):       
        for i in range(0 + 1, I):
         u[i][j + 1] = (u[i][j] + lam * u[i - 1][j + 1] + r * fun_f(x[i], t[j])) / (1 + lam)
         
# Схема 4 для [прямоугольной][rect]области. a > 0
def scheme_4_rect_a_pos(u, a, I, x, J, t, lam, fun_f):   
    for j in range(J - 1):       
        for i in range(0 + 1, I):           
            fc = fun_f(x[i] + h / 2, t[j] + r / 2)
            u[i][j + 1] = (u[i - 1][j] * (1 + lam) + (u[i][j] - u[i - 1][j + 1]) * (1 - lam) + 2 * r * fc) / (1 + lam)
            
# Схема 4 для [прямоугольной][rect]области. a < 0
def scheme_4_rect_a_neg(u, a, I, x, J, t, lam, fun_f):   
    for j in range(J - 1):       
        for i in range(I - 1, 0, -1):  # a<0 обратный порядок
            fc = fun_f(x[i] + h / 2, t[j] + r / 2)
            u[i - 1][j + 1] = (2 * r * h * fc + h * (u[i - 1][j] + u[i][j] - u[i][j + 1]) - a * r * ( u[i][j] + u[i][j + 1] - u[i - 1][j])) / (h - a * r)


def scheme_1_case_1():   
    J = int((def_t_end - def_t_start) / r) + 1   
    x_start = def_x_start - J * h   
    I = int((def_x_end - x_start) / h) + 1   
    solve(
        title = "Схема 1. 1 случай. \nОДНОРОДНОЕ, полуплоскость, a > 0",
        I = I,       
        x_start = x_start,       
        x_end = def_x_end,       
        J = J,
        t_start = def_t_start,       
        t_end = def_t_end,       
        a = a_pos,       
        fun_f = lambda x, t: 0,
        fun_u_x_0 = lambda x:  x**2 - 5*x + 5,
        fun_u_0_x = None,       
        fun_u_1_x = None,       
        scheme = scheme_1_halfplane_a_pos,   
    )
    
def scheme_1_case_2():   
    J = int((def_t_end - def_t_start) / r) + 1   
    x_start = def_x_start - J * h   
    I = int((def_x_end - x_start) / h) + 1   
    solve(
        title="Схема 1. 2 случай. \nНЕОДНОРОДНОЕ, полуплоскость, a > 0",
        I=I,       
        x_start=x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_pos,       
        fun_f= lambda x,t:x,
        fun_u_x_0=lambda x:  x**2 - 5*x + 5,
        fun_u_0_x=None,       
        fun_u_1_x=None,       
        scheme=scheme_1_halfplane_a_pos,   
    )

def scheme_1_case_3():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 1. 3 случай. \nОДНОРОДНОЕ, прямоугольная область, a > 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_pos,       
        fun_f=lambda x, t: 0,
        fun_u_x_0=lambda x:  x**2 + 5*x + 5,
        fun_u_0_x=lambda t: t**2 + 5*t + 5,
        fun_u_1_x=None,       
        scheme=scheme_1_rect_a_pos,   
    )
    
def scheme_1_case_4():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 1. 4 случай. \nНЕОДНОРОДНОЕ, прямоугольная область, a > 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_pos,       
        fun_f=lambda x, t: x,
        fun_u_x_0=lambda x:  x**2 + 5*x + 5,
        fun_u_0_x=lambda t:  t**2 + 5*t + 5,
        fun_u_1_x=None,       
        scheme=scheme_1_rect_a_pos,   
    )
    
def scheme_2_case_1():   
    J = int((def_t_end - def_t_start) / r) + 1   
    x_end = def_x_end + J * h   
    I = int((x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 2. 1 случай. \nОДНОРОДНОЕ, полуплоскость, a < 0",
        I=I,       
        x_start=def_x_start,       
        x_end=x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_neg,       
        fun_f=lambda x, t: 0,
        fun_u_x_0=lambda x:  x**2 - 5*x + 5,
        fun_u_0_x=None,       
        fun_u_1_x=None,       
        scheme=scheme_2_halfplane_a_neg,   
    )
    
def scheme_2_case_2():   
    J = int((def_t_end - def_t_start) / r) + 1   
    x_end = def_x_end + J * h   
    I = int((x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 2. 2 случай. \nНЕОДНОРОДНОЕ, полуплоскость, a < 0",
        I=I,       
        x_start=def_x_start,       
        x_end=x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_neg,       
        fun_f=lambda x, t: x,
        fun_u_x_0=lambda x:  x**2 - 5*x + 5,
        fun_u_0_x=None,       
        fun_u_1_x=None,       
        scheme=scheme_2_halfplane_a_neg,   
    )
    
def scheme_2_case_3():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 2. 3 случай. \nОДНОРОДНОЕ, прямоугольная область, a < 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_neg,       
        fun_f=lambda x, t: 0,
        fun_u_x_0=lambda x:  x**2 - 5*x + 5,
        fun_u_0_x=None,       
        fun_u_1_x=lambda t:  t**2 - 5*t + 1,
        scheme=scheme_2_rect_a_neg,   
    )
    
def scheme_2_case_4():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 2. 4 случай. \nНЕОДНОРОДНОЕ, прямоугольная область, a < 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_neg,       
        fun_f=lambda x,t: x,
        fun_u_x_0=lambda x:  x**2 - 5*x + 5,
        fun_u_0_x=None,       
        fun_u_1_x=lambda t: t**2 - 5*t + 1,
        scheme=scheme_2_rect_a_neg,   
    )
    
def scheme_3_case_1():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 3. 1 случай. \nОДНОРОДНОЕ прямоугольная область, a > 0",
        I=I,       
        x_start=def_x_start,    
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_pos,       
        fun_f=lambda x, t: 0,
        fun_u_x_0=lambda x:  x**2 + 5*x + 5,
        fun_u_0_x=lambda t:  t**2 + 5*t + 5,
        fun_u_1_x=None,       
        scheme=scheme_3_rect_a_pos,   
    )
    
def scheme_3_case_2():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 3. 2 случай. \nНЕОДНОРОДНОЕ, прямоугольная область, a > 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_pos,       
        fun_f=lambda x, t: x,
        fun_u_x_0=lambda x:  x**2 + 5*x + 5,
        fun_u_0_x=lambda t:  t**2 + 5*t + 5,
        fun_u_1_x=None,       
        scheme=scheme_3_rect_a_pos,   
    )
    
def scheme_4_case_1():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 4. 1 случай. \nОДНОРОДНОЕ, прямоугольная область, a > 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_pos,       
        fun_f=lambda x, t: 0,
        fun_u_x_0=lambda x:  x**2 + 5*x + 5,
        fun_u_0_x=lambda t:  t**2 + 5*t + 5,
        fun_u_1_x=None,       
        scheme=scheme_4_rect_a_pos,   
    )
    
def scheme_4_case_2():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 4. 2 случай. \nНЕОДНОРОДНОЕ, прямоугольная область, a > 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_pos,       
        fun_f=lambda x, t: x,
        fun_u_x_0=lambda x:  x**2 + 5*x + 5,
        fun_u_0_x=lambda t:  t**2 + 5*t + 5,
        fun_u_1_x=None,
        scheme=scheme_4_rect_a_pos,   
    )
    
def scheme_4_case_3():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 4. 3 случай. \nОДНОРОДНОЕ, прямоугольная область, a < 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_neg,       
        fun_f=lambda x, t: 0,
        fun_u_x_0=lambda x:  x**2 -5*x + 5,
        fun_u_0_x=None,
        fun_u_1_x=lambda t:  t**2 -5*t + 1,
        scheme=scheme_4_rect_a_neg,   
    )

def scheme_4_case_4():   
    J = int((def_t_end - def_t_start) / r) + 1   
    I = int((def_x_end - def_x_start) / h) + 1   
    solve(
        title="Схема 4. 4 случай. \nНЕОДНОРОДНОЕ, прямоугольная область, a < 0",
        I=I,       
        x_start=def_x_start,       
        x_end=def_x_end,       
        J=J,       
        t_start=def_t_start,       
        t_end=def_t_end,       
        a=a_neg,       
        fun_f=lambda x, t: x,
        fun_u_x_0=lambda x:  x**2 -5*x + 5,
        fun_u_0_x=None,
        fun_u_1_x=lambda t:  t**2 -5*t + 1,
        scheme=scheme_4_rect_a_neg,
    )

precision = 6

a_pos = 2
a_neg = -a_pos

def_x_start = 0
def_x_end = 1
def_t_start = 0
def_t_end = 10

h = 0.1
r = 0.04


plots_color_theme = ("winter")
np.set_printoptions(linewidth=100, precision=precision, suppress=True, floatmode="fixed")

#Для схемы 1
scheme_1_case_1()
scheme_1_case_2()
scheme_1_case_3()
scheme_1_case_4()

#Для схемы 2
scheme_2_case_1()
scheme_2_case_2()
scheme_2_case_3()
scheme_2_case_4()

#Для схемы 3
scheme_3_case_1()
scheme_3_case_2()

#Для схемы 4
scheme_4_case_1()
scheme_4_case_2()
scheme_4_case_3()
scheme_4_case_4()

plt.show()
