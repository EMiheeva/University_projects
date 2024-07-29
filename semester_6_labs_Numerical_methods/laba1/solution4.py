'''
Конечноразностный метод Ньютона
'''
import numpy as np
def function(x):
    return 2 * np.exp(-x) - x / 2
def final_newton_method(x_previous, h, epsilon):
    print(f"итерация k\tx[k] решение")
    k = 0
    print(f'итерация {k}: x[{k+1}] = {x_previous:.7f}')
    while True:
        x_next = x_previous - (h * function(x_previous)) / (function(x_previous + h) - function(x_previous))
        k += 1
        print(f'итерация {k}: x[{k+1}] = {x_next:.7f}')
        if abs(x_next - x_previous) < epsilon:
            return x_next
        x_previous = x_next

eps = 1e-7
answer = final_newton_method(1, 0.1, eps)
print(f"Результат: {answer:.7f}")
