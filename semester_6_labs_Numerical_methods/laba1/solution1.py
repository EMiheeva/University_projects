'''
Метод Ньютона (Метод касательных)
'''
import numpy as np
def function(x):
    return 2 * np.exp(-x) - x / 2
def diff_function(x):
    return -2 * np.exp(-x) - 1 / 2
def newton_method(x_0, epsilon):
    k = 0
    x_previous = x_0
    print("итерация k\tx[k] решение")
    # x_next - x_(k+1)
    # x_previous - x_(k)
    print(f"итерация {k}: x[{k+1}] = {x_previous:.7f} - выбранное нами")
    while True:
        k += 1
        x_next = x_previous - function(x_previous) / diff_function(x_previous)
        print(f"итерация {k}: x[{k+1}] = {x_next:.7f}")
        if abs(x_next - x_previous) < epsilon:
            break
        x_previous = x_next
    return x_next

eps = 1e-7
answer = newton_method(1, eps)
print(f"Результат: {answer:.7f}")

