'''
Метод простых итераций
'''
import numpy as np
def function(x):
    return -2 * np.exp(-x) + x / 2
def simple_iterations_method(a, b, epsilon):
    print(f"итерация k\tx[k] решение")
    t = 1
    x_previous = a
    k = 0
    print(f'итерация {k}: x[{k + 1}] = {x_previous:.7f}')
    while True:
        x_next = x_previous - t * function(x_previous)
        k += 1
        print(f'итерация {k}: x[{k+1}] = {x_next:.7f}')
        if abs(x_next - x_previous) < epsilon:
            return x_next
        x_previous = x_next

eps = 1e-7
answer = simple_iterations_method(1, 2, eps)
print(f"Результат: {answer:.7f}")
