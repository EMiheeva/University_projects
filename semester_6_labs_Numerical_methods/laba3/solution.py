'''
1. Метод левых прямоугольников  
2. Метод правых прямоугольников  
3. Метод средних прямоугольников  
4. Метод трапеций  
5. Метод Симпсона  
'''
import numpy as np
from scipy import integrate

a = 0
b = np.pi/2

def f(x):
    return 1 / (1 + np.sin(x))

def F(x):
    return -2 / (1 + np.tan(x / 2))

epsilon = 1e-4
step = 10

def formula_h(a, b, n):
    return (b - a) / n

def double_recalculation(coefficient, integral_1, integral_2):
    if coefficient * np.abs(integral_1 - integral_2) < epsilon:
        return False
    return True 
    
def relative_accuracy(true_solution, approximate_solution):
    return np.abs(true_solution - approximate_solution) * 100 / true_solution

def rectangle_left_calculation(a, b, n):
    h = formula_h(a, b, n)
    array_x_i = np.arange(a, b, h)
    sum_x_i = sum(f(x) for x in array_x_i)
    return h * sum_x_i  #ФОРМУЛА

#true_solution = F(b) - F(a)
true_solution, _ = integrate.quad(f, a, b)
def rectangle_left_method(a, b, n):
    coefficient = 1
    count_point = n * 2
    
    integral_1 = rectangle_left_calculation(a, b, n)
    integral_2 = rectangle_left_calculation(a, b, count_point)
    
    while double_recalculation(coefficient, integral_1, integral_2):
        n = count_point
        count_point = n * 2
        integral_1 = rectangle_left_calculation(a, b, n)
        integral_2 = rectangle_left_calculation(a, b, count_point)

    print(f'1) Заданная точность {epsilon}'
          f'\n2) Точное решение {true_solution:.4f} '
          f'\n3) Полученное приближенное решение(Ответ) с заданной точностью: {integral_2:.4f} '
          f'\n3)* Это же полученное приближенное решение с большей точностью, чем указанная: {integral_2:.10f} '
          f'\n4) Величина последнего шага интегрирования: {formula_h(a, b, count_point)} '
          f'\n5) Количество точек разбиения: {count_point} '
          f'\n6) Относительная погрешность метода: {relative_accuracy(true_solution, integral_2):.10f}%')


print("Первый метод - метод левых прямоугольников")
rectangle_left_method(a, b, step)


print()

def rectangle_right_int(a, b, n):
    h = formula_h(a, b, n)
    array_x_i = np.arange(a + h, b + h, h)
    sum_x_i = sum(f(x) for x in array_x_i)
    return h * sum_x_i #формула
    
def rectangle_right_method(a, b, n):
    coefficient = 1
    count_point = n * 2

    integral_1 = rectangle_right_int(a, b, n)
    integral_2 = rectangle_right_int(a, b, count_point)

    while double_recalculation(coefficient, integral_1, integral_2):
        n = count_point
        count_point = n * 2
        integral_1 = rectangle_right_int(a, b, n)
        integral_2 = rectangle_right_int(a, b, count_point)

    print(f'1) Заданная точность {epsilon}'
          f'\n2) Точное решение {true_solution:.4f} '
          f'\n3) Полученное приближенное решение(Ответ) с заданной точностью: {integral_2:.4f} '
          f'\n3)* Это же полученное приближенное решение с большей точностью, чем указанная: {integral_2:.10f} '
          f'\n4) Величина последнего шага интегрирования: {formula_h(a, b, count_point)} '
          f'\n5) Количество точек разбиения: {count_point} '
          f'\n6) Относительная погрешность метода: {relative_accuracy(true_solution, integral_2):.10f}%')

print("Второй метод - метод правых прямоугольников")
rectangle_right_method(a, b, step)

print()

def rectangle_middle_calculation(a, b, n):
    h = formula_h(a, b, n)
    array_x_i = np.arange(a, b, h)
    sum_x_i = sum(f(x + h/2) for x in array_x_i) #формула
    return h * sum_x_i
    
def rectangle_middle_method(a, b, n):
    coefficient = 1
    count_point = n * 2

    integral_1 = rectangle_middle_calculation(a, b, n)
    integral_2 = rectangle_middle_calculation(a, b, count_point)

    while double_recalculation(coefficient, integral_1, integral_2):
        n = count_point
        count_point = n * 2
        integral_1 = rectangle_middle_calculation(a, b, n)
        integral_2 = rectangle_middle_calculation(a, b, count_point)

    print(f'1) Заданная точность {epsilon}'
          f'\n2) Точное решение {true_solution:.4f} '
          f'\n3) Полученное приближенное решение(Ответ) с заданной точностью: {integral_2:.4f} '
          f'\n3)* Это же полученное приближенное решение с большей точностью, чем указанная: {integral_2:.10f} '
          f'\n4) Величина последнего шага интегрирования: {formula_h(a, b, count_point)} '
          f'\n5) Количество точек разбиения: {count_point} '
          f'\n6) Относительная погрешность метода: {relative_accuracy(true_solution, integral_2):.10f}%')

print("Третий метод - метод средних прямоугольников")
rectangle_middle_method(a, b, step)

print()
def trapezoidal_calculation(a, b, n):
    h = formula_h(a, b, n)
    array_x_i = np.arange(a, b, h)
    array_x_i = np.delete(array_x_i, 0)
    sum_x_i = sum(f(x) for x in array_x_i)
    return h * ((f(a)+f(b))/2 + sum_x_i) #формула
    
def trapezoidal_method(a, b, n):
    coefficient = 1/3
    count_point = n * 2
    integral_1 = trapezoidal_calculation(a, b, n)
    integral_2 = trapezoidal_calculation(a, b, count_point)

    while double_recalculation(coefficient, integral_1, integral_2):
        n = count_point
        count_point = n * 2
        integral_1 = trapezoidal_calculation(a, b, n)
        integral_2 = trapezoidal_calculation(a, b, count_point)

    print(f'1) Заданная точность {epsilon}'
          f'\n2) Точное решение {true_solution:.4f} '
          f'\n3) Полученное приближенное решение(Ответ) с заданной точностью: {integral_2:.4f} '
          f'\n3)* Это же полученное приближенное решение с большей точностью, чем указанная: {integral_2:.10f} '
          f'\n4) Величина последнего шага интегрирования: {formula_h(a, b, count_point)} '
          f'\n5) Количество точек разбиения: {count_point} '
          f'\n6) Относительная погрешность метода: {relative_accuracy(true_solution, integral_2):.10f}%')

print("Четвертый метод - метод трапеций")
trapezoidal_method(a, b, step)

print()

def simpson_calculation(a, b, n):
    h = formula_h(a, b, n)
    array_x_2i = np.arange(a + 2*h, b, 2* h)
    array_x_2i_1 = np.arange(a + h, b, 2* h)
    sum_x_2i = sum(f(x) for x in array_x_2i)
    sum_x_2i_1 = sum(f(x) for x in array_x_2i_1)
    return (h / 3) * (f(a) + 2 * sum_x_2i + 4 * sum_x_2i_1 + f(b)) #формула
    
def simpson_method(a, b, n):
    coefficient = 1/15
    count_point = n * 2

    integral_1 = simpson_calculation(a, b, n)
    integral_2 = simpson_calculation(a, b, count_point)

    while double_recalculation(coefficient, integral_1, integral_2):
        n = count_point
        count_point = n * 2
        integral_1 = simpson_calculation(a, b, n)
        integral_2 = simpson_calculation(a, b, count_point)

    print(f'1) Заданная точность {epsilon}'
          f'\n2) Точное решение {true_solution:.4f} '
          f'\n3) Полученное приближенное решение(Ответ) с заданной точностью: {integral_2:.4f} '
          f'\n3)* Это же полученное приближенное решение с большей точностью, чем указанная: {integral_2:.10f} '
          f'\n4) Величина последнего шага интегрирования: {formula_h(a, b, count_point)} '
          f'\n5) Количество точек разбиения: {count_point} '
          f'\n6) Относительная погрешность метода: {relative_accuracy(true_solution, integral_2):.10f}%')

print("Пятый метод - метод Симпсона")
simpson_method(a, b, step)
