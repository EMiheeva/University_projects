'''
Метод Хорд
'''
import numpy as np
def function(x):
    return 2 * np.exp(-x) - x / 2
def chord_method(a, b, epsilon):
    k = 0
    # x_next - x_(k+1)
    # x_previous - x_(k)
    print("итерация к\tx[k] решение")
    x_previous = a - ((b - a) * function(b)) / (function(b) - function(a))
    print(f"итерация {k}: x[{k + 1}] = {x_previous:.7f}")
    x_next = x_previous - (function(x_previous) * (b - x_previous)) / (function(b) - function(x_previous))
    while True:
        k += 1
        x_previous, x_next = x_next, x_next - (function(x_next) * (b - x_next)) / (function(b) - function(x_next))
        print(f'итерация {k}: x[{k+1}] = {x_previous:.7f}')
        if abs(x_next - x_previous) < epsilon:
            break
    return x_next

eps = 1e-7
answer = chord_method(1, 2, eps)
print(f"Результат: {answer:.7f}")
